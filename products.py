class ProductCategory:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"Category: {self.name} - {self.description}")
        for product in self.products:
            print(f"{product.name} - {product.description}")
            
class Product:
    def __init__(self, name, description):
        self.name = name
        self.description = description