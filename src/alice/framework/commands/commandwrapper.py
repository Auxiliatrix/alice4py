from abc import ABC, abstractmethod
from alice.main import constants
from alice.framework.events.directors import CommandDirector

class CommandWrapper(ABC):
    """
    An abstract static wrapper class for Discord4py commands.
    This allows commands to be associated with a class, and
    also utilize inherited utility functions, such as help messages.
    """
    
    @property
    @abstractmethod
    def name():
        pass

    @property
    @abstractmethod
    def command_function():
        pass

    @classmethod
    def invocation(cls):
        """
        Returns the invocation token.

        :return: String representing the invocation token.
        """

        return f"{constants.PREFIX}{cls.name}"

    @classmethod
    def invoked(cls, *payload):
        """
        Determines whether the attached command would be invoked.

        :return: True if command would be invoked by the payload; False otherwise.
        """

        return payload[0].content.split(' ')[0].lower() == cls.invocation().lower()
    
    @classmethod
    def attach(cls, director: CommandDirector, bot):
        """
        Attaches this Command to a director and a bot.

        :param director: CommandDirector to attach to. Notifies director when invoked.
        :param bot: Bot to register this command with.
        """
        
        director._commands.append(cls)
        bot.add_command(cls.command_function)