from alice.framework.events.types import EventType
from alice.framework.events.handlers import EventHandler

class ReadyHandler(EventHandler):
    """
    Handler to execute all necessary preprocessing
    once the client has logged in to Discord.
    """

    def __init__(self):
        super().__init__(EventType.READY)
    
    def handle(self, *payload):
        print(f"Logged in.")