from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self, new_data):
        pass
