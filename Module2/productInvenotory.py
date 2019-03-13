from json import dumps, loads


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def to_dic(self):
        return { "name": self.name, "price": self.price }

def totalProducts(products):
    total=0.0
    for product in products:
        total+=product.price
    print("You have products total value of:{} \n\n",format(total))

def addProduct(name, price):
    new_product = Product(name, price)
    products.append(new_product)


def listProduct(products):
    for p in products:
        print("Product name [{}] : Price ${} ".format(p.name, p.price))

def loadProducts():
    try:
        productFile=open("product.json","r+")
    except IOError:
        return []
    product_json=productFile.read()
    product_info=loads(product_json)
    products=[]
    for product in product_info:
        products.append(Product(product["name"],product["price"]))
    productFile.close()
    return products
def saveProduct(products):
    productSavedList = []
    for product in products:
        productSavedList.append(product.to_dic())
    productFile = open("product.json", "w+")
    productFile.write(dumps(productSavedList))
    productFile.close()

products = loadProducts()
while True:
    print("Type 'add' to add a product")
    print("Type 'list' to see list of all products")
    print("Type 'quit' to quit the program")
    command = input("Type a command: ")
    if command == "quit":
        saveProduct(products)
        break
    if command == "add":
        product_name = input("Enter a name of product: ")
        try:
            product_price = float(input("Enter a price for this product: "))
        except ValueError:
            print("enter valid value")
            continue
        addProduct(product_name, product_price)
    if command == "list":
        listProduct(products)
    if command=="total":
        totalProducts(products)
