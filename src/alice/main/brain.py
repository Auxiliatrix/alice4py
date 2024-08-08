import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"..",".."))

from alice.framework.events.types import EventType
from alice.framework.events.directors import EventDirector, CommandDirector
from alice.modular.handlers.readyhandler import ReadyHandler
from alice.modular.commands.pingcommand import PingCommand

from alice.main.namespace import client

ALICE_TOKEN = os.getenv("ALICE_TOKEN","")   # Get token from environment

if len(ALICE_TOKEN) == 0:
    raise Exception("Missing environment variable: \"ALICE_TOKEN\"")

if __name__ == "__main__":
    # Establish event directors, register with client, and attach handlers
    ready_director = EventDirector(EventType.READY)
    ready_director.register_hook(client)
    ReadyHandler().attach(ready_director)

    command_director = CommandDirector()
    ready_director.register_hook(client)
    PingCommand.attach(command_director, client)

    # Run bot
    client.startup(ALICE_TOKEN)
