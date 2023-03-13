from abc import ABC, abstractmethod


class GenericTask(ABC):

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def perform(self):
        pass
