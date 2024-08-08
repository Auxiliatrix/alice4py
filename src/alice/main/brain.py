import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"..",".."))

from alice.framework.events.base.eventtype import EventType
from alice.framework.events.directors.eventdirector import EventDirector
from alice.framework.events.directors.commanddirector import CommandDirector
from alice.modular.handlers.readyhandler import ReadyHandler
from alice.modular.commands.pingcommand import PingCommand

from alice.main.namespace import client

ALICE_TOKEN = os.getenv("ALICE_TOKEN","")

if len(ALICE_TOKEN) == 0:
    raise Exception("Missing environment variable: \"ALICE_TOKEN\"")

if __name__ == "__main__":
    # TODO: this might be better structured if it attached to the client
    ready_director = EventDirector(EventType.READY)
    ready_director.register_hook(client)
    ReadyHandler().attach(ready_director)

    command_director = CommandDirector()
    ready_director.register_hook(client)
    PingCommand.attach(command_director, client)

    client.startup(ALICE_TOKEN)
