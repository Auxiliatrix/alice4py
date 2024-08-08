from abc import ABC, abstractmethod
from alice.main import constants
from alice.framework.events.directors import CommandDirector

class CommandWrapper(ABC):
    
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
        return f"{constants.PREFIX}{cls.name}"

    @classmethod
    def invoked(cls, *payload):
        return payload[0].content.split(' ')[0].lower() == cls.invocation().lower()
    
    @classmethod
    def attach(cls, director: CommandDirector, client):
        director._commands.append(cls)
        client.add_command(cls.command_function)