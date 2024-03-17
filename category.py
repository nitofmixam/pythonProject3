class Category:
    """
    Класс для категорий товара
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def get_products(self):
        return self.__products

    @property
    def get_products_formatted(self):
        formatted_products = []
        for product in self.__products:
            formatted_products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return formatted_products
