# MCFETCH
Fetches Minecraft player information from the Mojang API

## Usage
1. `pip install mcfetch`
2. Use the module like this:

### API
```python
>>> from mcfetch import FetchPlayer
>>> player = FetchPlayer(name="gronkh")
>>> player.name
'Gronkh'
>>> player.uuid
'a2080281c2784181b961d99ed2f3347c'
```

You can also start from an existing UUID:

```python
>>> from mcfetch import FetchPlayer
>>> player = FetchPlayer(uuid="a2080281c2784181b961d99ed2f3347c")
>>> player.name
'Gronkh'
```

If a player doesn't exist:
```python
>>> from mcfetch import FetchPlayer
>>> player = FetchPlayer(name="ThisUsernameIsNotValid")
>>> player.name
None
>>> player.uuid
None
```

It is also possible to use a custom requests object:
```python
>>> from mcfetch import FetchPlayer
>>> from requests_cache import CachedSession
>>> my_cache = CachedSession(cache_name='./my_cache', expire_after=60)
>>> player = FetchPlayer(name="gronkh", requests_obj=my_cache)
```

### Tools
Check syntax of a username:

```python
>>> from mcfetch import is_valid_username
>>> is_valid_username('gronkh')
True
>>> is_valid_username('gronkh-is cool')
False
```

Check syntax of a UUID (undashed):

```python
>>> from mcfetch import is_valid_uuid
>>> is_valid_uuid('a2080281c2784181b961d99ed2f3347c')
True
>>> is_valid_uuid('bcc28a5f6')
False
```

Remove dashes from a UUID:

```python
>>> from mcfetch import undash_uuid
>>> undash_uuid('a2080281-c278-4181-b961-d99ed2f3347c')
a2080281c2784181b961d99ed2f3347c
```

## License
This software is licensed under the MIT license. Feel free to use it however you like.
