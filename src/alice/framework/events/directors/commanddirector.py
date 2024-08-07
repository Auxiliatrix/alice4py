from alice.framework.events.base.eventtype import EventType
from alice.framework.commands.commandwrapper import CommandWrapper
from alice.framework.events.handlers.messagehandler import MessageHandler
from alice.framework.events.directors.eventdirector import EventDirector

class CommandDirector(EventDirector):

    def __init__(self, client):
        self._commands = []
        super().__init__(client, EventType.MESSAGE)
    
    def direct(self, *payload):
        invoked = False
        for command in self._commands:
            if command.invoked(payload):
                invoked = True
                break
        for handler in self._handlers:
            if not invoked or not handler.recessive:
                handler.handle(payload)

    def attach(self, attachee):
        if isinstance(attachee, CommandWrapper):
            self._commands.append(attachee)
            self._client.command_hook.add_command(attachee.command_function)
        else:
            if not isinstance(attachee, MessageHandler):
                raise TypeError(f"'attachee' must be an object of type 'MessageHandler', not '{type(attachee)}'.")
            self._handlers.append(attachee)