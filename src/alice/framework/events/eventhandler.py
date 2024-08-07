from abc import ABC, abstractmethod
from alina.utils.generic import Generic

class EventHandler(Generic, ABC):
    
    def __init__(self, event_type):
        self._event_type = event_type

    @abstractmethod
    def handle(payload):
        """
        Handle the payload of a given event received from Discord.

        :param payload: Event payload to process.
        :return: Function to be executed in response to the payload.
        """
        return lambda: None
    
    def generic(self):
        return self._event_type

    # TODO: python annotation for help messages?