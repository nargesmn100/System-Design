# Design a Shopping Cart System:
# Implement a basic shopping cart where users can add products, remove products, and view the total price. Each product should have an ID, name, and price.

# We will first make a Products class, then use the Shopping cart class to inherit all products. 
class Product():
    def __init__(self, id, name, price):
        self.product_id = id
        self.product_name = name
        self.product_price = price


class Shopping_Cart(Product):
    def __init__(self):
        self.cart = []

    def add_products(self, product):
        self.cart.append(product)

    def remove_products(self, product_id):
        # Assuming that we want to remove products based on their id.
        # Don't modify the list and iterate over it at the same time; indexing backward doesn't change index!
        for item_placement in range(len(self.cart) -1, -1, -1):
            if self.cart[item_placement] == product_id:
                del self.cart[item_placement]

    def view_total_price(self):
        total = 0
        for item in self.cart:
            total += item.product_price
        return "\n".join([f"Your total is ${total} dollars."])
    
    def cart_contents(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
        
        product_lst = []
        for i, item in enumerate(self.cart):
            product_lst.append(f"Item number {i + 1}: {item.product_name}")
        return "\n".join(product_lst)


# Test
prod_1 = Product(1, "Cartier Love Ring", 1000)
prod_2 = Product(2, "Givenchy Boots", 5500)
cart = Shopping_Cart()
cart.add_products(prod_1)
cart.add_products(prod_2)
print(cart.cart_contents())
print(cart.view_total_price())
cart.remove_products(prod_1)
print(cart.cart_contents())