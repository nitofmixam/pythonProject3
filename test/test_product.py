import pytest
from product import Product, Smartphone, LawnGrass, Order


# Тест на создание экземпляра класса Product
def test_smartphone_inheritance():
    phone = Smartphone("iPhone", "Смартфон", 100_000,
                       10, 32, "X", 128, "Space Gray")
    assert isinstance(phone, Product)


def test_product_addition_different_class():
    product1 = Product("Product1", "Описание", 100, 10)
    product2 = LawnGrass("Grass1", "Описание", 150, 15, "USA",
                         "Месяц", "Зеленый")
    with pytest.raises(TypeError):
        result = product1 + product2


