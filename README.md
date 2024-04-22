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
>>> from mcfetch import Player
>>> player = Player(player="gronkh")
>>> player.name
'Gronkh'
>>> player.uuid
'a2080281c2784181b961d99ed2f3347c'
```

Fetch a player using their uuid:

```python
>>> from mcfetch import Player
>>> player = Player(player="a2080281c2784181b961d99ed2f3347c")
>>> player.name
'Gronkh'
```

If a player doesn't exist:

```python
>>> from mcfetch import Player
>>> player = Player(player="ThisUsernameIsNotValid")
>>> player.name
None
>>> player.uuid
None
```

It is also possible to use a custom requests object:

```python
>>> from mcfetch import Player
>>> from requests_cache import CachedSession
>>> my_cache = CachedSession(cache_name='./my_cache', expire_after=60)
>>> player = Player(player="gronkh", requests_obj=my_cache)
```

You can fetch a player's skin URL and skin texture

```python
>>> from mcfetch import Player
>>> player = Player(player="Notch")
>>> player.skin_url
'http://textures.minecraft.net/texture/292009a4925b58f02c77dadc3ecef07ea4c7472f64e0fdc32ce5522489362680'
>>> player.skin_texture
b'\x89PNG\r\n\x1a\n\x00\x00\x00\...'
```

### Asynchronous

Fetching a player (same functionality as the above examples)

```python
>>> import asyncio
>>> from mcfetch import AsyncPlayer
>>> async def main():
...     player = AsyncPlayer(player="Gronkh")
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
'a2080281c2784181b961d99ed2f3347c'
```

Added dashes to a UUID:

```python
>>> from mcfetch import dash_uuid
>>> dash_uuid('a2080281c2784181b961d99ed2f3347c')
'a2080281-c278-4181-b961-d99ed2f3347c'
```

## License

This software is licensed under the MIT license. Feel free to use it however you like. For more infomation see [LICENSE](https://github.com/oDepleted/mcfetch/blob/master/LICENSE).
