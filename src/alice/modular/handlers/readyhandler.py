from alice.main import constants
from alice.framework.events.base.eventtype import EventType
from alice.framework.events.handlers.eventhandler import EventHandler

class ReadyHandler(EventHandler):

    def __init__(self):
        super().__init__(EventType.READY)
    
    def handle(self, *payload):
        print(f"Logged in.")