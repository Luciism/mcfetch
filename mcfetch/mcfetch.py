import json
from base64 import b64decode

import requests


class Player:
    def __init__(
        self,
        player: str,
        requests_obj=requests
    ):
        """
        Initializes a Player object with a name or uuid.

        Args:
            player (str): The player's username or uuid.
            requests_obj (module, optional): The requests module or a compatible
            object to use for making HTTP requests. Defaults to the requests module.

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

        self._requests_obj = requests_obj


    @property
    def name(self) -> str | None:
        """Returns the player's pretty name."""
        if self._pretty_name is None:
            if self._name is None:
                self._load_by_uuid()
            else:
                self._load_by_name()
        return self._pretty_name


    @property
    def uuid(self) -> str | None:
        """Returns the player's uuid."""
        self._load_by_name()
        return self._uuid


    @property
    def skin_url(self) -> str | None:
        """Returns the player's skin url."""
        if self._skin_url is None:
            if self._uuid is None:
                self._load_by_name()
            self._load_by_uuid()
        return self._skin_url


    @property
    def skin_texture(self) -> str | None:
        """Returns the player's skin texture images as bytes."""
        if self._skin_texture is None:
            if self.skin_url is None:
                return None
            self._skin_texture = self._requests_obj.get(self.skin_url).content
        return self._skin_texture


    def _load_by_name(self):
        if self._uuid is None and self._player_exists:
            data: dict = self._requests_obj.get(
                f"https://api.mojang.com/users/profiles/minecraft/{self._name}").json()

            self._uuid = data.get("id")
            self._pretty_name = data.get("name")

            if self._pretty_name is None:
                self._player_exists = False


    def _load_by_uuid(self):
        if (not self._has_loaded_by_uuid) and self._player_exists:
            data: dict = self._requests_obj.get(
                f"https://sessionserver.mojang.com/session/minecraft/profile/{self._uuid}"
            ).json()

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
