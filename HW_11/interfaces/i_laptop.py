from abc import ABC, abstractmethod


class ILaptop(ABC):

    @abstractmethod
    def _include(self):
        pass

    @abstractmethod
    def _charge(self, battery):
        pass

    @abstractmethod
    def _turn_off(self):
        pass
