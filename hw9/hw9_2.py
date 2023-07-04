class Car:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if isinstance(value, str):
            self._brand = value
        else:
            print("Brand field is empty")

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str):
        if len(self._model) > 0:
            self._model = value
        else:
            print("Model field is empty")

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if self._price > 0 and type(self.price) is float:
            self._price = value
        else:
            print("Fields filled incorrectly")

    @classmethod
    def from_dict(cls, car_dict):
        return cls(
            brand=car_dict.get("brand"),
            model=car_dict.get("model"),
            price=car_dict.get("price")
        )

    def get_car_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}\n"
    @staticmethod
    def year_sale(year: int):
        if year > 2008 and year < 2018:
            return f"You can buy a car of the {year} year of manufacture with a 20% discount!"
        else:
            return f"There are no discounts for cars of the {year} year of manufacture!"

if __name__ == '__main__':
    car = Car("Honda", "Civic", 75100.00)
    print(car.get_car_info())

    car_dict = {
    'brand': "Toyota",
    'model': 'RAV4',
    'price': 125000.00
    }
    car_from_dict = Car.from_dict(car_dict)
    print(car_from_dict.get_car_info())
    car = Car.year_sale(2015)
    print(car)
