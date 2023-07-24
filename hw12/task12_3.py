class Iterator:
    def __init__(self, sequence: list):
        self.__sequence = sequence
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < len(self.__sequence):
            element = self.__sequence[self.__current]
            self.__current += 1
            return element
        else:
            raise StopIteration


if __name__ == '__main__':
    iterator_new = Iterator([1, 2, 3, 4, 5, 6, 7, 8])
    for element in iterator_new:
        print(element)
