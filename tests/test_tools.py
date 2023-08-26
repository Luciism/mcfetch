from mcfetch import is_valid_username, is_valid_uuid, undash_uuid


def test_valid_username_with_valid_username():
    assert is_valid_username('Notch')

def test_valid_username_with_invalid_username():
    assert not is_valid_username('...---...')

def test_valid_uuid_with_valid_uuid():
    assert is_valid_uuid('069a79f444e94726a5befca90e38aaf5')

def test_valid_uuid_with_invalid_uuid():
    assert not is_valid_username('not a valid uuid')

def test_undash_uuid():
    dashed = '069a79f4-44e9-4726-a5be-fca90e38aaf5'
    undashed = undash_uuid(dashed)
    assert undashed.find('-') == -1
