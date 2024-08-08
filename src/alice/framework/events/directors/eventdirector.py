from alina.utils.typing.generic import Generic
from alice.framework.events.base.eventtype import EventType

class EventDirector(Generic):

    def __init__(self, event_type: EventType):
        self._event_type = event_type
        self._handlers = []

    def register_hook(self, client):
        hook_name = f"on_{self._event_type.value}"
        setattr(self, hook_name, self.direct)
        hook = getattr(self, hook_name)
        hook.__func__.__name__ = hook_name
        hook.__func__.__qualname__ = f"{__class__.__qualname__}.{hook_name}"
        client.event(hook)

    async def direct(self, *payload):
        for handler in self._handlers:
            handler.handle(*payload)

    def generic(self):
        return self._event_type

    # TODO: some kind of override for how different handler types are handled
    # TODO: maybe if a handler requires preprocessing, that's done first