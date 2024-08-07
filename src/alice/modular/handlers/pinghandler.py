from alice.main import constants
from alice.framework.events.eventtype import EventType
from alice.framework.events.eventhandler import EventHandler

class PingHandler(EventHandler):
    
    def __init__(self):
        super().__init__(EventType.MESSAGE)
    
    def handle(payload):
        if payload.content.split[' '][0] == f"{constants.PREFIX}ping":
            print("Pong!")