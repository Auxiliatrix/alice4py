from abc import ABC, abstractmethod
from alice.main import constants

class CommandWrapper(ABC):

    def __init__(self, name, command_function):
        self.name = name
        self.command_function = command_function
    
    def invocation(self):
        return f"{constants.PREFIX}{self.name}"

    def invoked(self, *payload):
        return payload[0].content.split(' ')[0].lower() == self.invocation().lower()