import pytest
from product import Product


# Тест на создание экземпляра класса Product
def test_product_instance():
    product = Product("Laptop", "High-performance laptop", 999.99, 10)
    assert product.name == "Laptop"
    assert product.description == "High-performance laptop"
    assert product.price == 999.99
    assert product.quantity == 10


def test_set_price_negative():
    product = Product("Phone", "Smartphone", 800, 5)
    product.price = -500
    assert product.price == 800  # Цена не изменилась из-за ошибки


