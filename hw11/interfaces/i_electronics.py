from abc import ABC, abstractmethod


class IElectronics(ABC):

    @abstractmethod
    def _software_update(self):
        pass
