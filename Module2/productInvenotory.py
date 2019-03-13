class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price


def addProduct(name, price):
    new_product = Product(name, price)
    products.append(new_product)


def listProduct(products):
    for p in products:
        print("Product name [{}] : Price ${} ".format(p.name, p.price))


products = []
while True:
    print("Type 'add' to add a product")
    print("Type 'list' to see list of all products")
    print("Type 'quit' to quit the program")
    command = input("Type a command: ")
    if command == "quit":
        break
    if command == "add":
        product_name = input("Enter a name of product: ")
        product_price = float(input("Enter a price for this product: "))
        addProduct(product_name, product_price)
    if command == "list":
        listProduct(products)
