from product_cart  import Item

class ProductCategory:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return f" The products available in the cart are: {self.products}"

    def remove_product(self, product):
        self.products.remove(product)
        return f"The products remaining in the cart are: {self.products}"

    def display_products(self):
        for product in self.products:
            print(product.name, product.description, product.price)
            print("This is a {product.description} {product.name} that costs {product.price}. ")