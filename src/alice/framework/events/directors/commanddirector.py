from alice.framework.events.base.eventtype import EventType
from alice.framework.events.directors.eventdirector import EventDirector

class CommandDirector(EventDirector):

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