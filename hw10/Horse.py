from Animals import Animals


class Horse(Animals):
    def __init__(self, name: str, age: int, food: str):
        super().__init__(name, age)
        self._food = food

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, new_food):
        if isinstance(food, str) and len(new_food) < 25:
            self._food = new_food
        else:
            print(f'The field with the name of the food must be a string and not exceed 25 characters')

    def additional_inventory(self):
        print(f"{self.name} need a saddle to ride on top.")

    def does(self):
        print(f"{self.name} engaged in the transport of small goods.")


if __name__ == '__main__':
    horse = Horse("Riman", 3, "Grass")
    horse.additional_inventory()
    horse.food = "Beet"
