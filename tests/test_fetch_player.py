from mcfetch import Player
from requests_cache import CachedSession


class _TestPlayerBase:
    def setup_method(self):
        self.existing_player = self.get_existing_player_instance()
        self.non_existing_player = self.get_non_existing_player_instance()

    def test_fetch_player_init(self):
        assert self.existing_player

    def test_fetch_player_uuid_by_existing_player(self):
        assert self.existing_player.uuid is not None

    def test_fetch_player_name_by_existing_player(self):
        assert self.existing_player.name is not None

    def test_fetch_player_name_by_non_existing_player(self):
        assert self.non_existing_player.name is None

    def test_fetch_player_skin_url_by_existing_player(self):
        assert self.existing_player.skin_url is not None

    def test_fetch_player_skin_url_by_non_existing_player(self):
        assert self.non_existing_player.skin_url is None

    def test_fetch_player_skin_texture_by_existing_player(self):
        assert self.existing_player.skin_texture is not None

    def test_fetch_player_skin_texture_by_non_existing_player(self):
        assert self.non_existing_player.skin_texture is None



class TestPlayerByName(_TestPlayerBase):
    def get_existing_player_instance(self):
        return Player(player='Notch')

    def get_non_existing_player_instance(self):
        return Player(player='Bitch')


class TestPlayerByUUID(_TestPlayerBase):
    def get_existing_player_instance(self):
        return Player(player='069a79f444e94726a5befca90e38aaf5')

    def get_non_existing_player_instance(self):
        return Player(player='abcdefghijklmnopqrstuvwxyz')



session = CachedSession(cache_name='.cache/test', expire_after=60)

class TestPlayerByNameWithCaching(_TestPlayerBase):
    def get_existing_player_instance(self):
        return Player(player='Notch', requests_obj=session)

    def get_non_existing_player_instance(self):
        return Player(player='Bitch', requests_obj=session)


class TestPlayerByUUIDWithCaching(_TestPlayerBase):
    def get_existing_player_instance(self):
        return Player(
            player='069a79f444e94726a5befca90e38aaf5', requests_obj=session)

    def get_non_existing_player_instance(self):
        return Player(
            player='abcdefghijklmnopqrstuvwxyz', requests_obj=session)
