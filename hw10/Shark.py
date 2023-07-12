from Fish import Fish


class Shark(Fish):
    def __init__(self, name: str, age: int, fish_for_food: str, view: str):
        super().__init__(name, age, fish_for_food)
        self._view = view

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, new_view):
        if isinstance(new_view, str) and len(new_view) < 15:
            self._view = new_view
        else:
            print(f'The field with the name of the view must be a string and not exceed 15 characters')

    def safety(self):
        print(f"{self.name} dangerous and can attack people.")

    def does(self):
        print(f"{self.name} predator that lives in the seas and oceans.")


if __name__ == '__main__':
    shark = Shark("Lola", 4, "Roach", "Tiger shark")
    shark.safety()
    shark.view = "Mako shark"
