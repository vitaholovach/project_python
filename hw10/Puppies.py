from Labrador1 import Labrador


class Puppies(Labrador):
    def __init__(self, name: str, age: int, ears: str, grooming: str,
                 document: str):
        super().__init__(name, age, ears, grooming)
        self._document = document

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, new_document):
        if isinstance(new_document, str):
            self._document = new_document
        else:
            print(f'The new document must be in string format.')

    def cynologist(self):
        print(f"{self.name} need to work with a cynologist.")

    def does(self):
        print(f"{self.age} still sleeping a lot.")


if __name__ == '__main__':
    puppies = Puppies("Molli", 2, "Short", "Haircut", "Certificate")
    puppies.document = "Passport"
    puppies.cynologist()
