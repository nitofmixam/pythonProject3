class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @staticmethod
    def create_product(name, price, quantity):
        return Product(name, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Ошибка: Цена введена некорректно. Цена должна быть больше нуля.")

