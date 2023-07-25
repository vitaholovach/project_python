class Iphone:
    def __init__(self, model: str, price: int, color: str):
        self.model = model
        self.price = price
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}:\n{{\nmodel: {self.model},\nprice: ${self.price},\ncolor: {self.color}\n}}"


if __name__ == '__main__':
    iphone = Iphone("Apple iPhone 14 Pro", 1200, "Black")
    print(iphone)
