from Shark import Shark


class Fish(Shark):
    def __init__(self, name: str, age: int, view: str, fish_for_food: str):
        super().__init__(name, age, view)
        self._fish_for_food = fish_for_food

    @property
    def fish_for_food(self):
        return self._fish_for_food

    @fish_for_food.setter
    def fish_for_food(self, new_fish_for_food):
        if isinstance(new_fish_for_food, str) and len(new_fish_for_food) < 10:
            self._fish_for_food = new_fish_for_food
        else:
            print(f'The field with the name of the fish for food must be a string and not exceed 10 characters')

    def cooking_method(self):
        print(f"{self.name} can be fried or baked {self.fish_for_food}.")

    def does(self):
        print(f"{self.name} live in rivers and seas")


if __name__ == '__main__':
    fish = Fish("Asad", 1, "River fish", "Pike")
    fish.cooking_method()
    fish.fish_for_food = "Salmon"
