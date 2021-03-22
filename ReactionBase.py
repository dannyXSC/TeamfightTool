from abc import ABCMeta, abstractmethod


class ReactionBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def setConfig(self, config):
        pass

    @abstractmethod
    def getInfo(self):
        pass

    @abstractmethod
    def processInfo(self, info):
        pass

    @abstractmethod
    def opration(self, info):
        pass

    @abstractmethod
    def end(self):
        pass
