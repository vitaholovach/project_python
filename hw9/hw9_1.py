class Apple:
    def __init__(self, name, product, types_of_electronics):
        self.name = name
        self._product = product
        self._types_of_electronics = types_of_electronics

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, str):
            self._product = value
        else:
            raise ValueError("Fill in the field in string format")

    @property
    def types_of_electronics(self):
        return self._types_of_electronics

    @types_of_electronics.setter
    def types_of_electronics(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._types_of_electronics = value
        else:
            raise ValueError("Fill in the field in string format")

    @classmethod
    def company_info(cls, name, product, types_of_electronics):
        if name or product or types_of_electronics is str:
            return cls(name, product, types_of_electronics)
        else:
            print('Fields filled incorrectly')
    def about_company(self):
        return f"Company: {self.name}, Product: {self._product}, Types of electronics: {self._types_of_electronics}"

    @staticmethod
    def product_price(gadget: str) -> float:
        price = {'Apple iPhone 14': 1800.00,
                 'Apple iPhone 13': 1600.00,
                 'Apple iPhone 12': 1200.50,
                 'Apple iPhone 11': 1320.00,
                 'Apple iPhone 10': 855.00,}
        if gadget in price.keys():
            return f'Price {gadget} is ${price.get(gadget)}'
        else:
            return f"To find out the cost, select a phone model."


if __name__ == '__main__':
    company = Apple("Apple", "Electronics", "iPad")
    print(company.about_company())
    company = Apple.product_price('Apple iPhone 12')
    print(company)
