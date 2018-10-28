""" Username to UUID
Converts a Minecraft username to it's UUID equivalent.

Uses the official Mojang API to fetch player data.
"""

### Import necessary modules
import http.client
import json
from tools import is_valid_minecraft_username
from tools import is_valid_mojang_uuid

### Main class
class GetPlayerData:
    def __init__(self, identifier, timestamp=None):
        self.valid = True
        """
            Get the UUID of the player.

            Parameters
            ----------
            username: string
                The known minecraft username
            timestamp : long integer (optional)
                The time at which the player used this name, expressed as a Unix timestamp.
        """

        # Handle the timestamp
        get_args = ""
        if timestamp is not None:
            get_args = "?at=" + str(timestamp)

        req = ""
        if is_valid_minecraft_username(identifier):
            req = "/users/profiles/minecraft/" + identifier + get_args
        elif is_valid_mojang_uuid(identifier):
            req = "/user/profiles/" + identifier + "/names" + get_args
        else:
            self.valid = False

        if self.valid:
            # Request the UUID
            http_conn = http.client.HTTPSConnection("api.mojang.com");
            http_conn.request("GET", req,
                headers={'User-Agent':'https://github.com/clerie/mcuuid', 'Content-Type':'application/json'});
            response = http_conn.getresponse().read().decode("utf-8")

            # In case the answer is empty, the user dont exist
            if not response:
                self.valid = False
            # If there is an answer, fill out the variables
            else:
                # Parse the JSON
                json_data = json.loads(response)
                if is_valid_minecraft_username(identifier):
                    # The UUID
                    self.uuid = json_data['id']
                    # The username written correctly
                    self.username = json_data['name']
                elif is_valid_mojang_uuid(identifier):
                    # The UUID
                    self.uuid = identifier

                    if timestamp is None:
                        timestamp = 0

                    current_name = ""
                    current_time = 0

                    # Getting the current username
                    for name in json_data:
                        if 'changedToAt' in name:
                            changed_to_at = name['changedToAt']
                        else:
                            changed_to_at = 0

                        if changed_to_at <= timestamp and current_time <= changed_to_at:
                            current_time = changed_to_at
                            current_name = name['name']

                    # The username written correctly
                    self.username = name['name']
