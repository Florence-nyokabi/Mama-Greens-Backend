from products import Product

class ProductCategory:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(product.name, product.description, product.price)