class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print("=============== Product details ===========================")
        print(f"Prodcut ID :{self.product_id}")
        print(f"Name :{self.name}")
        print(f"Price: {self.price}")

class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
    
    def display(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self,product):
        self.items.append(product)
        print(f"{product.name} added to Cart")

    def view_cart(self):
        print("------------------Shopping Product--------------------")
        total = 0
        if not self.items:
            print("cart is Empty")
            return 
        for product in self.items:
            print(f"{product.name} - {product.price}")
            total+=product.price
        print(f"Total Amount: {total}")
     

    def get_total(self):
        total=0
        for product in self.items:
            total += product.price
        return total

class Order:
    def __init__(self,customer,cart):
        
        self.customer = customer
        self.cart = cart


    def place_order(self):
        subtotal = self.cart.get_total()

        if subtotal >= 50000:
            discount = subtotal * 0.10 # 10%
        elif subtotal >= 30000:
            discount = subtotal * 0.08 #8%
        elif subtotal >= 20000:
            discount = subtotal * 0.05 #5%
        else:
            discount = 0

        shipping_charge = 100
        payable_amount = subtotal - discount + shipping_charge

        print("=================== Order Summmary =====================")
        self.customer.display()
        print("--------------------------------------------------")
        print("== Purchased Products")
        for product in self.cart.items:
            print(f"{product.name}-{product.price}")
        print("---------------- Customer Details---------------------")
        print(f"Subtotal : {subtotal}")
        print(f"Discount: {discount}")
        print(f"Shipping Charge: {shipping_charge}")

        print("------------_-------------------------------------------")

        print(f"Payable Amount: {payable_amount}") 
        print("Order Placed Successfully")


product1 = Product(101, "laptop",60000)
product2 = Product(102 , "heatphone", 20000)
product3 = Product(103 , "Mobile", 40000)
product4 = Product(104 , "earbots", 5000)

customer = Customer(1 , "Gagan Gowda Ku")

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)

cart.add_product(product4)

order = Order(customer, cart)
order.place_order()
    