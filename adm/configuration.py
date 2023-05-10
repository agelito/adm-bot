import os

class Configuration:
    """App configuration variables"""

    def __init__(self):
        self.discord_token = os.getenv('DISCORD_TOKEN')
        self.alliance_id = int(os.getenv('ALLIANCE_ID'))

    def __str__(self):
        return '{}(discord_token={}, alliance_id={})'.format(
            self.__class__.__name__, self.discord_token, self.alliance_id
        )
