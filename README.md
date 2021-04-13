# MCUUID
Getting Minecraft Player Information from Mojang API.

## Usage
1. `pip install mcuuid`
2. Use the module like this:

### API
```
> from mcuuid import MCUUID
> player = MCUUID(name="gronkh")
> player.name
'Gronkh'
> player.names
{0: 'Gronkh'}
> player.uuid
'a2080281c2784181b961d99ed2f3347c'
```

You can also use an existing uuid to start from:

```
> player = MCUUID(uuid="a2080281c2784181b961d99ed2f3347c")
> player.name
'Gronkh'
```

### Tools
Check syntax of an username:

```
>from mcuuid.tools import is_valid_minecraft_username
> is_valid_minecraft_username('gronkh'):
True
```

Check syntax of an UUID:

```
> from mcuuid.tools import is_valid_mojang_uuid
> is_valid_mojang_uuid('a2080281c2784181b961d99ed2f3347c'):
True
```

### Version information
There is a wrapper around the new MCUUID class to still be usable using former api versions.
They are deprecated and not recommended for future use.

## License
This software is licensed under the MIT license. Feel free to use it however you like.
