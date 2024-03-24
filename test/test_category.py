import pytest
from category import Category
from product import Product


def test_get_products_formatted():
    category = Category("Electronics", "Category for electronic devices")
    product1 = Product("Laptop", "High-performance laptop", 999.99, 10)
    product2 = Product("Smartphone", "Flagship smartphone", 799.99, 20)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = [
        "Laptop, 999.99 руб. Остаток: 10 шт.",
        "Smartphone, 799.99 руб. Остаток: 20 шт."
    ]

    assert category.get_products_formatted == expected_output


def test_category_str():
    c = Category("Товар", "Описание")
    assert str(c) == "Товар, количество продуктов: 0 шт."


def test_add_product():
    cat = Category("Товар", "Описание")
    assert len(cat.get_products) == 0
    product = Product("Товар", "Описание", 50, 10)
    cat.add_product(product)
    assert len(cat.get_products) == 1


