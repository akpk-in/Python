class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self, quantity):
        return self.stock >= quantity
    
    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity):
        if product.is_available(quantity):
            self.items.append({
                'product': product,
                'quantity': quantity
            })
            return f"Added {quantity} {product.name}(s)"
        return "Out of stock"
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
    
    def checkout(self):
        for item in self.items:
            item['product'].reduce_stock(item['quantity'])
        total = self.get_total()
        self.items = []
        return f"Order completed! Total: ${total}"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
    
    def add_to_cart(self, product, quantity):
        return self.cart.add_item(product, quantity)
    
    def view_cart(self):
        if not self.cart.items:
            return "Cart is empty"
        items = []
        for item in self.cart.items:
            items.append(f"{item['quantity']}x {item['product'].name}")
        return f"Cart: {', '.join(items)}"
    
    def place_order(self):
        return self.cart.checkout()

# Usage
laptop = Product("Laptop", 1000, 5)
mouse = Product("Mouse", 25, 10)

customer = Customer("John", "john@email.com")
print(customer.add_to_cart(laptop, 1))  # Added 1 Laptop(s)
print(customer.add_to_cart(mouse, 2))   # Added 2 Mouse(s)
print(customer.view_cart())             # Cart: 1x Laptop, 2x Mouse
print(customer.place_order())           # Order completed! Total: $1050