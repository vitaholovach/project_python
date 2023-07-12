from Horse import Horse


class Pony(Horse):
    def __init__(self, name: str, age: int, food: str, height: str):
        super().__init__(name, age, food)
        self._height = height

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, new_height):
        if isinstance(new.height, str) and len(new_height) < 160:
            self._height = new.height
        else:
            print(f"The field average horse weight must be a string and not higher 160")

    def weight(self):
        print(f"{self.name} small, heavily built stocky pony {self.height}.")

    def does(self):
        print(f"{self.name} horseback riding for children.")


if __name__ == '__main__':
    pony = Pony("Pip", 4, "Grass", "120")
    pony.weight()
    pony.height = "135"
