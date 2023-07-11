from Dog import Dog


class Labrador(Dog):
    def __init__(self, name: str, age: int, residence: str, ears: str, grooming: str):
        super().__init__(name, age, residence, ears)
        self._grooming = grooming

    @property
    def grooming(self):
        return self._grooming

    @grooming.setter
    def grooming(self, new_grooming):
        if new_grooming == "Trimming" or new_grooming == "Rolling":
            self._grooming = new_grooming
        else:
            print(f'The new grooming should be "Cutting" or "Rolling", but the actual result is {new_grooming}')

    def procedure(self):
        print(f"{self.name} doing the procedure {self.grooming}.")

    def does(self):
        print(f"{self.name} playing with children")


if __name__ == '__main__':
    labrador = Labrador("Rich", 4, "Home or street", "Hanging", "Сreative")
    labrador.procedure()
    labrador.grooming = "Hygienic"
