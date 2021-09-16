from abc import ABC, abstractmethod


class Abstract_writer(ABC):
    def __init__(self, path=""):
        self.data = {}
        self.path = path

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def encode_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass
