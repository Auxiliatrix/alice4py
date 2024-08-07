import os

from alice.framework.events.base.eventtype import EventType
from alice.framework.events.directors.eventdirector import EventDirector
from alice.framework.events.directors.commanddirector import CommandDirector
from alice.modular.handlers.readyhandler import ReadyHandler
from alice.modular.commands.pingcommand import PingCommand

from aliceclient import AliceClient

ALICE_TOKEN = os.getenv("ALICE_TOKEN","")

if len(ALICE_TOKEN) == 0:
    raise Exception("Missing environment variable: \"ALICE_TOKEN\"")

if __name__ == "__main__":
    client = AliceClient(ALICE_TOKEN)

    # TODO: this might be better structured if it attached to the client
    ready_director = EventDirector(client, EventType.READY)
    ready_director.attach(ReadyHandler())

    command_director = CommandDirector(client)
    command_director.attach(PingCommand())

    client.startup()

    # TODO: handle messagehandlers not interfering with commands
    # either wrap commands into messagehandlers
    # or find a static solution