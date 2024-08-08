from abc import ABC, abstractmethod
from alina.utils.typing.generic import Generic
from alice.framework.events.types import EventType
from alice.framework.events.directors import EventDirector

class EventHandler(Generic, ABC):
    """
    Abstract class to handle a given event type.
    """
    
    def __init__(self, event_type):
        self._event_type = event_type

    @abstractmethod
    def handle(self, *payload):
        """
        Handle the payload of a given event received from Discord.

        :param payload: Event payload to process.
        """

        pass
    
    def attach(self, director: EventDirector):
        """
        Attaches this handler to an EventDirector, allowing 
        coordination between EventHandler objects.

        :param director: EventDirector to attach to.
        """

        if director.generic() != self.generic():
            raise TypeError(f"Imcompatible event types: '{self.generic()}' and '{director.generic()}'.")
        director._handlers.append(self)

    def generic(self):
        return self._event_type

    # TODO: python annotation for help messages?

class MessageHandler(EventHandler, ABC):
    """
    EventHandler subclass specifically designed to handle message events.
    """

    def __init__(self, recessive=True):
        self.recessive = recessive

        super().__init__(EventType.MESSAGE)