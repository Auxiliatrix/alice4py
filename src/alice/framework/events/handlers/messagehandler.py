from abc import ABC, abstractmethod
from enum import Enum
from alice.main import constants
from alice.framework.events.base.eventtype import EventType
from alice.framework.events.handlers.eventhandler import EventHandler

class MessageHandler(EventHandler, ABC):

    def __init__(self, recessive=True):
        self.recessive = recessive

        super().__init__(EventType.MESSAGE)