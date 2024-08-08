from alina.utils.typing.generic import Generic
from alice.framework.events.types import EventType

class EventDirector(Generic):
    """
    An event manager that determines which handlers should activate
    in response to a given event type.
    """

    def __init__(self, event_type: EventType):
        self._event_type = event_type
        self._handlers = []

    def register_hook(self, client):
        """
        Subscribes this to a Discord client.

        :param client: Client to subscribe to.
        """

        # TODO: also store registration on the client
        hook_name = f"on_{self._event_type.value}"
        setattr(self, hook_name, self.direct)
        hook = getattr(self, hook_name)
        hook.__func__.__name__ = hook_name
        hook.__func__.__qualname__ = f"{__class__.__qualname__}.{hook_name}"
        client.event(hook)

    async def direct(self, *payload):
        """
        Manages which handlers respond to the provided payload.

        :param payload: Arguments provided by the event trigger.
        """

        for handler in self._handlers:
            handler.handle(*payload)

    def generic(self):
        return self._event_type

    # TODO: some kind of override for how different handler types are handled
    # TODO: maybe if a handler requires preprocessing, that's done first

class CommandDirector(EventDirector):
    """
    EventDirector subclass specifically to handle message events and commands.
    Ensures that most message events do not trigger when a command is invoked.
    """

    def __init__(self):
        self._commands = []
        self._registered = False
        super().__init__(EventType.MESSAGE)
    
    def register_hook(self, client):
        if not self._registered:
            async def direct_wrapper(self, *payload):
                result = self.direct_wrapper(*payload)
                await client.process_commands(*payload)
                return result
            self.direct = direct_wrapper
            self._registered = True
        super().register_hook(client)

    async def direct(self, *payload):
        invoked = False
        for command in self._commands:
            if command.invoked(*payload):
                invoked = True
                break
        for handler in self._handlers:
            if not invoked or not handler.recessive:
                handler.handle(*payload)