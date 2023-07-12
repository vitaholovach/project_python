from Dog import Dog


class ShepherdDog(Dog):
    def __init__(self, name: str, age: int, ears: str, grooming: str, residence: str):
        super().__init__(name, age, ears, grooming)
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
        print(f'{self.name} eat bones')

    def does(self):
        print(f'{self.name} protects the house')


if __name__ == '__main__':
    shepherdDog = ShepherdDog("Mira", 1, "Sticking", "Hygienic", "Home")
    shepherdDog.eat_food()
    shepherdDog.does()
