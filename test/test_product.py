import pytest
from product import Product, Smartphone, LawnGrass


# Тест на создание экземпляра класса Product
def test_smartphone_inheritance():
    phone = Smartphone("iPhone", "Смартфон", 100_000,
                       10, 32, "X", 128, "Space Gray")
    assert isinstance(phone, Product)


def test_lawn_grass_creation():
    lawn_grass = LawnGrass("Lawn Grass", "Описание", 20, 100, "USA",
                           "Месяц", "Зеленый")
    assert lawn_grass.name == "Lawn Grass"
    assert lawn_grass.description == "Описание"
    assert lawn_grass._Product__price == 20
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "Месяц"
    assert lawn_grass.color == "Зеленый"


def test_product_creation():
    product = Product("Продукт", "Описание", 100, 10)
    assert product.name == "Продукт"
    assert product.description == "Описание"
    assert product._Product__price == 100
    assert product.quantity == 10


def test_product_addition_different_class():
    product1 = Product("Product1", "Описание", 100, 10)
    product2 = LawnGrass("Grass1", "Описание", 150, 15, "USA",
                         "Месяц", "Зеленый")
    with pytest.raises(TypeError):
        result = product1 + product2

