from product_cart  import Item

class ProductCategory:
    def __init__(self, name, description, price,category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return f" You have added some products into the cart. currently the products available in the cart are: {self.products}"

    def remove_product(self, product):
        self.products.remove(product)
        return f" You have removed {product} from the cart and now the products remaining in the cart are: {self.products}"

    def display_of_products(self):
        for product in self.products:
            print(product.name, product.description, product.price)
            print("This is a {product.description} {product.name} that costs {product.price}. ")
    
    def display_category_products(self):
        for product in self.products:
            print(product.name, product.description, product.price, product.category)
            print("This is a {product.description} {product.name} in the category{product.category}and it costs {product.price}. ")