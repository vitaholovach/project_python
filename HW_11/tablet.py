from hw11.interfaces.i_laptop import ILaptop
from hw11.interfaces.i_electronics import IElectronics


# abstraction, inheritance
class Tablet(ILaptop, IElectronics):

    def __init__(self):
        self.__status = True
        self.__installing_an_update = True
        self.__battery_power = 1

    # abstraction, polymorphism
    def _include(self):
        self.__status = True
        print("Tablet ready to go")

    # abstraction, polymorphism
    def _software_update(self):
        print("New software version available")

    # incapsulation, abstraction, polymorphism
    def _charge(self, battery: int):
        if battery > 35:
            print("Charging is enough. Keep using your tablet")
        else:
            print("Tablet power saving mode")
        self.__battery_power = battery

    # abstraction, polymorphism
    def _turn_off(self):
        self.__status = True
        print("Job completed!")

    # incapsulation
    def launch(self, battery_power: int):
        self._include()
        self._software_update()
        self._charge(battery_power)
        self._turn_off()


if __name__ == '__main__':
    tablet = Tablet()
    tablet.launch(64)
