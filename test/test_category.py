import pytest
from category import Category


# Тест на создание экземпляра класса Category с продуктами
def test_category_instance_with_products():
    products = ["Laptop", "Smartphone", "Headphones"]
    category = Category("Electronics", "Category for electronic devices", products)
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category.products == products


# Тест на увеличение счетчика продуктов
def test_product_count_increase():
    initial_count = Category.product_count
    products = ["T-Shirt", "Jeans"]
    Category("Clothing", "Category for clothing items", products)
    assert Category.product_count == initial_count + len(products)
