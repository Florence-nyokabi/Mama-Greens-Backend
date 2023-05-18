class Grocery:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.grocery_items = []
        self.total_price = 0
    
    def add_item(self, grocery_item):
        self.grocery_items.append(grocery_item)
        self.total_price += grocery_item.price
    
    def remove_item(self, grocery_item):
        self.grocery_items.remove(grocery_item)
        self.total_price -= grocery_item.price
    
    def view_order(self):
        print(f"Customer Name: {self.customer_name}")
        for item in self.grocery_items:
            print(f"Item Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
        print(f"Total Price: {self.total_price}")
    
# grocery1 = Grocery("mango", 10, 100)
# grocery2 = Grocery("mango", 10, 100)

# order1 = Order("Florence Nyokabi")

# order1.add_item(grocery1)
# order1.add_item(grocery2)
# order1.view_order()