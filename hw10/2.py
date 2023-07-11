from Animals import Animals


class Cat(Animals):
    def __init__(self, name: str, age: int, residence: str):
        super().__init__(name, age)
        self._residence = residence

    @property
    def residence(self):
        return self._residence

    @residence.setter
    def residence(self, new_residence):
        if isinstance(new_residence, str):
            self._residence = new_residence
        else:
            print('Fill in the field in string format')

    def eat_food(self):
        print(f'{self.name} eat mice')

    def does(self):
        print(f'{self.name} sleapin')


if __name__ == '__main__':
    cat = Cat("Mira", 1, "Home")
    cat.eat_food()
    cat.does()
