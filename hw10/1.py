from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print(f'Name should be a string')

    @abstractmethod
    def does(self):
        pass


if __name__ == '__main__':
    animals = Animals("All", 2)
