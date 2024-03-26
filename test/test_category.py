import pytest
from category import Category
from product import Product


def test_category_str():
    c = Category("Товар", "Описание")
    assert str(c) == "Товар, количество продуктов: 0 шт."


def test_add_product():
    cat = Category("Товар", "Описание")
    assert len(cat.get_products) == 0
    product = Product("Товар", "Описание", 50, 10)
    cat.add_product(product)
    assert len(cat.get_products) == 1


def test_category_creation():
    category = Category("Категория", "Описание")
    assert category.name == "Категория"
    assert category.description == "Описание"
    assert len(category.get_products) == 0


