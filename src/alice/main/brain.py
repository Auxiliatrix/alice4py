import os
from alice.framework.events.eventtype import EventType
from alice.framework.events.eventdirector import EventDirector
from alice.framework.events.eventhandler import EventHandler
from aliceclient import AliceClient

ALICE_TOKEN = os.getenv("ALICE_TOKEN","")

if len(ALICE_TOKEN) == 0:
    raise Exception("Missing environment variable: \"ALICE_TOKEN\"")

if __name__ == "__main__":
    client = AliceClient(ALICE_TOKEN)

    message_director = EventDirector(EventType.MESSAGE)
    message_director.attach(EventHandler(EventType.MESSAGE))

    client.startup()