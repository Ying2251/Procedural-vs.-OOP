class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)

    def show_products(self):
        print("List of products in the store:")
        for product in self.__products:
            print(f"- {product.name}: {product.quantity}  pieces")

# 🛒 สร้างร้านและเพิ่มสินค้า
my_store = Store()
my_store.add_product("Shampoo", 20)
my_store.add_product("Hair conditioner", 15)

# 📋 แสดงรายการสินค้า
my_store.show_products()