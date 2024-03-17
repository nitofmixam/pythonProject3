import pytest
from category import Category
from product import Product


def test_add_product():
    category = Category("Electronics", "Category for electronic products")
    product = Product("Smartphone", 500, 10, "Samsung")

    initial_product_count = Category.product_count
    category.add_product(product)
    assert len(category.get_products) == 1
    assert Category.product_count == initial_product_count + 1


