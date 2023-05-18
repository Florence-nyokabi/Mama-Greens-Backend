from products import Product

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        self.products.remove(product)

    def checkout(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

p1 = Product("mango", 10, "Fruit")
p2 = Product("cabbage", 50, "vagetable")
cart = ShoppingCart([p1, p2])