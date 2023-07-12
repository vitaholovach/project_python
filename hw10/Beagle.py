from Dog import Dog


class Beagle(Dog):
    def __init__(self, name: str, age: int, ears: str, price: int):
        super().__init__(name, age, ears)
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and len(new_price) < 850:
            self._price = new_price
        else:
            print(f'The cost per puppy should not exceed 850')

    def quality(self):
        print(f"{self.name} with a pedigree will cost {self.price}.")

    def does(self):
        print(f"{self.name} coexists perfectly at home and in the apartment")


if __name__ == '__main__':
    beagle = Beagle("Roni", 4, "Long", 325)
    beagle.quality()
    beagle.price = 120
