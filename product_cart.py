class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, products):
        self.products = []

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        self.products.remove(product)

    def checkout(self):
        total = 0
        for product in self.products:
            total += product.price
        return f" The total price for the products is:  {total}"

# item1 = Item("mango", 10, "Fruit")
# item2 = Item("cabbage", 50, "vagetable")
# cart = ShoppingCart([item1, item2])
# total_price = cart.checkout()
# print(total_price)