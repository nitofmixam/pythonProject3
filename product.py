class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: int, model: str, memory: float, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @staticmethod
    def create_product(name, __price, quantity):
        return Product(name, __price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, __price):
        if __price <= 0:
            print("Ошибка: Цена введена некорректно. Цена должна быть больше нуля.")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно складывать только товары одного класса")
        total_quantity = self.quantity + other.quantity
        return Product(f"{self.name} + {other.name}", self.price, total_quantity)

