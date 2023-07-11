from Cat import Cat


class Hare(Cat):
    def __init__(self, name: str, age: int, residence: str, weight: float):
        super().__init__(name, age, residence)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, float):
            self._weight = new_weight
        else:
            print('You made a mistake while filling out the field, please enter first')

    def coat_color(self):
        print(f"{self.name} skin color gray")

    def does(self):
        print(f"{self.name} running in the forest")


if __name__ == '__main__':
    hare = Hare("Lin", 2, "Forest", 230.10)
    hare.coat_color()
    hare.weight = 250.77
