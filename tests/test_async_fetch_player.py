import pytest

from aiohttp_client_cache import SQLiteBackend
from mcfetch import AsyncPlayer, RequestFailedError


class _TestAsyncPlayerBase:
    def setup_method(self):
        self.existing_player: AsyncPlayer = \
            self.get_existing_player_instance()

        self.non_existing_player: AsyncPlayer = \
            self.get_non_existing_player_instance()


    def test_fetch_player_init(self):
        assert self.existing_player

    @pytest.mark.asyncio
    async def test_fetch_player_uuid_by_existing_player(self):
        assert await self.existing_player.uuid is not None

    @pytest.mark.asyncio
    async def test_fetch_player_name_by_existing_player(self):
        assert await self.existing_player.name is not None

    @pytest.mark.asyncio
    async def test_fetch_player_name_by_non_existing_player(self):
        assert await self.non_existing_player.name is None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_url_by_existing_player(self):
        assert await self.existing_player.skin_url is not None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_url_by_non_existing_player(self):
        assert await self.non_existing_player.skin_url is None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_texture_by_existing_player(self):
        assert await self.existing_player.skin_texture is not None

    @pytest.mark.asyncio
    async def test_fetch_player_skin_texture_by_non_existing_player(self):
        assert await self.non_existing_player.skin_texture is None



class TestAsyncPlayerByName(_TestAsyncPlayerBase):
    def get_existing_player_instance(self):
        return AsyncPlayer(player='Notch')

    def get_non_existing_player_instance(self):
        return AsyncPlayer(player='Bitch')


class TestAsyncPlayerByUUID(_TestAsyncPlayerBase):
    def get_existing_player_instance(self):
        return AsyncPlayer(player='069a79f444e94726a5befca90e38aaf5')

    def get_non_existing_player_instance(self):
        return AsyncPlayer(player='abcdefghijklmnopqrstuvwxyz')



session = SQLiteBackend(cache_name='.cache/test', expire_after=60)

class TestAsyncPlayerByNameWithCaching(_TestAsyncPlayerBase):
    def get_existing_player_instance(self):
        return AsyncPlayer(player='Notch', cache_backend=session)

    def get_non_existing_player_instance(self):
        return AsyncPlayer(player='Bitch', cache_backend=session)


class TestAsyncPlayerByUUIDWithCaching(_TestAsyncPlayerBase):
    def get_existing_player_instance(self):
        return AsyncPlayer(
            player='069a79f444e94726a5befca90e38aaf5', cache_backend=session)

    def get_non_existing_player_instance(self):
        return AsyncPlayer(
            player='abcdefghijklmnopqrstuvwxyz', cache_backend=session)
