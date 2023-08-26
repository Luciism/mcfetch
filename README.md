# MCFETCH
Fetches Minecraft player information from the Mojang API

## Installation
Run the following:
```bash
pip install mcfetch
```
## How to use

### Non asynchronous
Fetch a player using their username:
```python
>>> from mcfetch import FetchPlayer
>>> player = FetchPlayer(name="gronkh")
>>> player.name
'Gronkh'
>>> player.uuid
'a2080281c2784181b961d99ed2f3347c'
```

Fetch a player using their uuid:

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

You can fetch a player's skin URL and skin texture
```python
>>> from mcfetch import FetchPlayer
>>> player = FetchPlayer(name="Notch")
>>> player.skin_url
'http://textures.minecraft.net/texture/292009a4925b58f02c77dadc3ecef07ea4c7472f64e0fdc32ce5522489362680'
>>> player.skin_texture
b'\x89PNG\r\n\x1a\n\x00\x00\x00\...'
```

Fetch a player without specifying whether you are using a Username or UUID
```python
>>> from mcfetch import FetchPlayer2
>>> player = FetchPlayer2("a2080281c2784181b961d99ed2f3347c")
>>> player.name
'Gronkh'
>>> player = FetchPlayer2("Gronkh")
>>> player.uuid
'a2080281c2784181b961d99ed2f3347c'
```


### Asynchronous
Fetching a player (same functionality as the above examples)
```python
>>> import asyncio
>>> from mcfetch import AsyncFetchPlayer2
>>> async def main():
...     player = AsyncFetchPlayer2("Gronkh")
...     print(await player.name)
...     print(await player.uuid)
>>> asyncio.run(main())
'Gronkh'
'a2080281c2784181b961d99ed2f3347c'
```


## Tools
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
This software is licensed under the MIT license. Feel free to use it however you like. For more infomation see [LICENSE](https://github.com/oDepleted/mcfetch/blob/master/LICENSE).
