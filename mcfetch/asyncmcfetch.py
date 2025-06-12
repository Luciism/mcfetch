import asyncio
import json
from base64 import b64decode
from typing import Any, Callable, Coroutine, TypeVar

from aiohttp import (
    ClientError,
    ClientSession,
    ClientTimeout,
    ContentTypeError,
    StreamReader,
    ClientResponse
)
from aiohttp_client_cache import CacheBackend, CachedSession

from .exceptions import RequestFailedError


class AsyncPlayer:
    def __init__(
        self,
        player: str,
        cache_backend: CacheBackend=None,
        request_retries: int=3,
        request_retry_delay: int=3,
        request_timeout: int=4
    ) -> None:
        """
        Initializes an AsyncPlayer object with a name or uuid.

        Args:
            player (str): The player's username or uuid.
            cache_backend (class, optional): The backend used for caching \
                responses, if `None`, caching won't be used.
            request_retries (int, optional): The amount of times to reattempt the \
                request if failed.
            request_retry_delay (int, optional): The delay (in seconds) to wait before \
                retrying the request
            request_timeout (int, optional): The amount of time to terminate the request \
                after if no response is delivered.

        Raises:
            AssertionError: If both name and uuid are None or if both are not None.
        """
        self._uuid = None
        self._name = None

        if len(player) > 16:
            self._uuid = player
        else:
            self._name = player

        self._pretty_name = None

        self._skin_url = None
        self._skin_texture = None

        self._player_exists = True
        self._has_loaded_by_uuid = False

        self.cache_backend = cache_backend

        self._request_retries = request_retries
        self._request_retry_delay = request_retry_delay
        self._request_timeout = request_timeout


    @property
    async def name(self) -> str | None:
        """Returns the player's pretty name."""
        if self._pretty_name is None:
            if self._name is None:
                await self._load_by_uuid()
            else:
                await self._load_by_name()
        return self._pretty_name


    @property
    async def uuid(self) -> str | None:
        """Returns the player's uuid."""
        await self._load_by_name()
        return self._uuid


    @property
    async def skin_url(self) -> str | None:
        """Returns the player's skin url."""
        if self._skin_url is None:
            if self._uuid is None:
                await self._load_by_name()
            await self._load_by_uuid()
        return self._skin_url


    @property
    async def skin_texture(self) -> str | None:
        """Returns the player's skin texture image as bytes."""
        if self._skin_texture is None:
            skin_url = await self.skin_url
            if skin_url is None:
                return None
            self._skin_texture = await self._make_request_with_err_handling(skin_url)

        return self._skin_texture


    ResponseT = TypeVar("T")
    async def _make_request(
        self,
        url: str,
        validator: Callable[[ClientResponse], Coroutine[Any, Any, ResponseT]]
    ) -> ResponseT:
        timeout = ClientTimeout(total=self._request_timeout)

        if self.cache_backend is None:
            async with ClientSession(timeout=timeout) as session:
                return await validator(await session.get(url))

        async with CachedSession(cache=self.cache_backend, timeout=timeout) as session:
            return await validator(await session.get(url))


    async def _make_request_with_err_handling(
        self,
        url: str,
        as_json: bool=False,
        _attempt: int=1
    ) -> dict | bytes:
        try:
            if as_json:
                return await self._make_request(url, lambda res: res.json())
            return await self._make_request(url, lambda res: res.content.read())

        except (TimeoutError, ClientError, ContentTypeError) as exc:
            if _attempt > self._request_retries:  # Max retries exceeded
                raise RequestFailedError(exc) from exc

            await asyncio.sleep(self._request_retry_delay)
            return await self._make_request_with_err_handling(
                url, as_json, _attempt=_attempt+1)


    async def _load_by_name(self):
        if self._uuid is None and self._player_exists:
            data = await self._make_request_with_err_handling(
                f"https://api.minecraftservices.com/minecraft/profile/lookup/name/{self._name}",
                as_json=True
            )

            self._uuid = data.get("id")
            self._pretty_name = data.get("name")

            if self._pretty_name is None:
                self._player_exists = False


    async def _load_by_uuid(self):
        if (not self._has_loaded_by_uuid) and self._player_exists:
            data = await self._make_request_with_err_handling(
                f"https://sessionserver.mojang.com/session/minecraft/profile/{self._uuid}",
                as_json=True
            )

            name = data.get("name")

            # Stops future requests
            if name is None:
                self._player_exists = False
                return
            self._pretty_name = name

            # Get skin url from base64 string
            for item in data.get('properties', []):
                if item.get('name') == 'textures':
                    encoded_str = item.get('value', '')
                    textures: dict = json.loads(b64decode(encoded_str) or '{}')

                    self._skin_url = textures.get('textures', {}).get('SKIN', {}).get('url')
                    break

            self._has_loaded_by_uuid = True
