from Animals1 import Animals


class Dog(Animals):
    def __init__(self, name: str, age: int, ears: str):
        super().__init__(name, age)
        self._ears = ears

    @property
    def ears(self):
        return self._ears

    @ears.setter
    def ears(self, new_ears):
        if new_ears == 'Long':
            self._ears = new_ears
        else:
            print(f'Expected response should be that the ears are long, got {new_ears} instead')

    def has(self):
        print(f"{self.name} it has ears {self._ears}.")

    def does(self):
        print(f"{self.name} stayting in an aviary.")


if __name__ == '__main__':
    dog = Dog("Ron", 5, "Long")
    dog.has()
    dog.ears = "Short"
