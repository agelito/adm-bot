import os

class Configuration:
    """App configuration variables"""

    def __init__(self):
        self.discord_token = os.getenv('DISCORD_TOKEN')
        self.discord_channel = os.getenv('DISCORD_CHANNEL')
        self.discord_app_id = os.getenv('DISCORD_APP_ID')

        alliance_id = os.getenv('ALLIANCE_ID')

        if alliance_id is not None:
            try:
                alliance_id = int(alliance_id)
            except ValueError as error:
                raise ValueError('[configuration] invalid `ALLIANCE_ID` value', alliance_id) from error

        self.alliance_id = alliance_id

    def __str__(self):
        return f'{self.__class__.__name__}(discord_token={self.discord_token}, discord_channel={self.discord_channel}, discord_app_id={self.discord_app_id}, alliance_id={self.alliance_id})'
