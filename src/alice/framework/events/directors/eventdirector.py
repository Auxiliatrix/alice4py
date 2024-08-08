from alina.utils.typing.generic import Generic
from alice.main.aliceclient import AliceClient
from alice.framework.events.handlers.eventhandler import EventHandler
from alice.framework.events.base.eventtype import EventType

class EventDirector(Generic):

    def __init__(self, client, event_type: EventType):
        self._client = client
        self._event_type = event_type
        self._handlers = []

        self.register_hook()

    def register_hook(self):
        hook_name = f"on_{self._event_type.value}"
        setattr(self, hook_name, self.direct)
        hook = getattr(self, hook_name)
        hook.__func__.__name__ = hook_name
        hook.__func__.__qualname__ = f"{__class__.__qualname__}.{hook_name}"
        self._client.event(hook)

    async def direct(self, *payload):
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