import discord, logging
from discord.ext import commands

from alice.main import constants

class AliceClient(discord.Client):
    """
    A wrapper class for discord.Client which manages the client connection
    and contains default presets for client initialization.
    """

    @staticmethod
    def _get_intents():
        """
        Builds AliceClient's default Discord Client intents.

        :return: discord.Intents object.
        """

        intents = discord.Intents.default()
        intents.message_content = True
        return intents

    def __init__(self):
        """
        Initializes the AliceClient Discord Client manager.
        """

        self.command_hook = commands.Bot(command_prefix=constants.PREFIX, intents=AliceClient._get_intents())

        super().__init__(intents=AliceClient._get_intents(), logging=self._get_logger())
    
    def _get_logger(self):
        """
        Builds a logger for the current instance of AliceClient.
        :return: logging.FileHandler object.
        """

        return logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    def startup(self, token):
        """
        Establishes a Discord Client connection with the given parameters.
        Starts up all necessary components.
        """

        self.run(token)
    
    def shutdown(self):
        """
        Shuts down the Discord Client connection and performs cleanup operations.
        """
        pass