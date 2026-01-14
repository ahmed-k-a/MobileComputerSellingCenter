from entity.product import Product

class ProductController:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)

    def get_products(self):
        return self.products
