def is_valid_username(username: str):
    """
    Check if a given string is a valid Minecraft username.

    A valid Minecraft username must be between 3 and 16 characters long and\n
    can only contain lowercase letters, numbers, and underscores.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    if not isinstance(username, str):
        return False

    allowed_chars = 'abcdefghijklmnopqrstuvwxyz1234567890_'
    min_len, max_len = 3, 16

    username = username.lower()

    if not min_len <= len(username) <= max_len:
        return False

    if not set(username).issubset(allowed_chars):
        return False

    return True


def is_valid_uuid(uuid: str):
    """
    Check if a given string is a valid Mojang UUID.

    A valid Mojang UUID must be 32 characters long and can only contain
    lowercase hexadecimal digits (0-9, a-f).

    Args:
        uuid (str): The UUID to check (undashed).

    Returns:
        bool: True if the UUID is valid, False otherwise.
    """
    if not isinstance(uuid, str):
        return False

    allowed_chars = '0123456789abcdef'
    allowed_len = 32

    uuid = uuid.lower().replace('-', '')

    if len(uuid) != allowed_len:
        return False

    if not set(uuid).issubset(allowed_chars):
        return False

    return True


def undash_uuid(uuid: str):
    """
    Remove dashes from a given UUID string.

    This function takes a UUID string, converts it to lowercase, and removes
    any dashes ('-') from it.

    Args:
        uuid (str): The UUID string to process.

    Returns:
        str: The UUID string with dashes removed.
    """
    uuid = uuid.lower()
    uuid = uuid.replace('-', '')
    return uuid


def dash_uuid(uuid: str):
    """
    Inserts dashes (-) at the standard positions in a UUID string.

    Args:
        uuid: A string representation of a UUID without dashes.

    Returns:
        A string representation of the UUID with dashes inserted.
    """
    if len(uuid) != 32:
        raise ValueError("Invalid UUID string length. Must be 32 characters.")

    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
