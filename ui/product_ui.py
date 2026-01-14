class ProductUI:
    def get_product_details(self):
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        return name, price, quantity

    def display_products(self, products):
        print("\nProduct List:")
        for p in products:
            print(f"- {p.name}, Price: {p.price}, Quantity: {p.quantity}")
