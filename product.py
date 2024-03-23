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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value


a = Product("a", "Товар", 10, 100)
b = Product("b", "Товар", 2, 200)
result = a + b
print(result)
