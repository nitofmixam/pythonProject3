class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @staticmethod
    def create_product(name, price, quantity):
        return Product(name, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, __price):
        if __price <= 0:
            print("Ошибка: Цена введена некорректно. Цена должна быть больше нуля.")

