from alice.framework.events.types import EventType
from alice.framework.events.handlers import EventHandler

class ReadyHandler(EventHandler):

    def __init__(self):
        super().__init__(EventType.READY)
    
    def handle(self, *payload):
        print(f"Logged in.")