### Import our module
from mcuuid.mcuuid import GetPlayerData

### Import some other necessary modules
import sys

### Which username should we use?
# Are there some arguments brought by the console use the first after the filename as username
if len(sys.argv) > 1:
    username = sys.argv[1]
# Else, ask for a username by userinput
else:
    print("Please enter a username: ")
    username = raw_input()

### Obtaining the playerinformation using our module
player = GetPlayerData(username)
# Check if the request was valid and the user exists
if player.valid is True:
    # Getting UUID
    uuid = player.uuid
    # Getting real Username
    name = player.username

    # Print everything
    print('UUID: ' + uuid)
    print('correct name: ' + name)
# Error message
else:
    print("That player was not found.")
