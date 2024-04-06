from abc import ABC, abstractmethod


class ReprMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        class_name = self.__class__.__name__
        return (f"Был создан объект: {class_name}\n"
                f"Атрибуты: {self.__dict__.items()}")


class Order(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass


class Product(Order, ReprMixin):

    def display_info(self):
        return f"Имя продукта: {self.name}, Цена: {self.__price}, Количество: {self.quantity}"

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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно складывать только товары одного класса")
        total_quantity = self.quantity + other.quantity
        return total_quantity


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: float, model: str, memory: float, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def display_info(self):
        return (f"Имя смартфона: {self.name}, Описание: {self.description} Цена: {self.__price}, /n "
                f"Количество: {self.quantity}, Модель: {self.model}, Память: {self.memory}, Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def display_info(self):
        return (f"Имя травы: {self.name}, Описание: {self.description} Цена: {self.__price}, /n "
                f"Количество: {self.quantity}, Страна: {self.country}, Период роста: {self.germination_period}, /n "
                f"Цвет: {self.color}")
