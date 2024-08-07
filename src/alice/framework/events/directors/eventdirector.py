from alina.utils.typing.generic import Generic
from alice.main.aliceclient import AliceClient
from alice.framework.events.handlers.eventhandler import EventHandler
from alice.framework.events.base.eventtype import EventType

class EventDirector(Generic):

    def __init__(self, client, event_type: EventType):
        self._client = client
        self._event_type = event_type
        self._handlers = []
        AliceClient.__dict__[f"on_{self._event_type}"] = self.direct


    def direct(self, *payload):
        for handler in self._handlers:
            handler.handle(payload)

    def attach(self, handler):
        if not isinstance(handler, EventHandler):
            raise TypeError(f"'handler' must be an object of type 'EventHandler', not '{type(handler)}'.")
        if handler.generic() != self.generic():
            raise TypeError(f"Imcompatible event types: '{self.generic()}' and '{handler.generic()}'.")
        self._handlers.append(handler)

    def generic(self):
        return self._event_type

    # TODO: some kind of override for how different handler types are handled
    # TODO: maybe if a handler requires preprocessing, that's done first