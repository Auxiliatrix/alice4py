import discord, logging
from discord.ext import commands

from alice.main import constants

class AliceClient(discord.Client):
    """
    A wrapper class for discord.Client which manages the client connection
    and contains default presets for client initialization.
    """

    @classmethod
    def _get_intents():
        """
        Builds AliceClient's default Discord Client intents.

        :return: discord.Intents object.
        """

        intents = discord.Intents.default()
        intents.message_content = True
        return intents

    def __init__(self, bot_token):
        """
        Initializes the AliceClient Discord Client manager.

        :param bot_token: String representing the Discord Bot token used to register this instantiation.
        """

        self._bot_token = bot_token
        self.command_hook = commands.Bot(command_prefix=constants.PREFIX, intents=AliceClient._get_intents())

        super().__init__(intents=AliceClient._get_intents())
    
    def _get_logger(self):
        """
        Builds a logger for the current instance of AliceClient.
        :return: logging.FileHandler object.
        """

        return logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    def startup(self):
        """
        Establishes a Discord Client connection with the given parameters.
        Starts up all necessary components.
        """

        self.run(logging=self._get_logger())
    
    def shutdown(self):
        """
        Shuts down the Discord Client connection and performs cleanup operations.
        """
        pass