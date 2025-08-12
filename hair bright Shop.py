import uuid

class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []          
        self.past_orders = []   

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []

    def addingItemsToCart(self, customer, product, quantity):
        customer.cart.append((product, quantity))

    def checkOut(self, customer):
        if not customer.cart:
            print("ไม่มีสินค้าในตะกร้า")
            return

        total_price = sum(product.price * quantity for product, quantity in customer.cart)
        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "items": [(product.name, quantity) for product, quantity in customer.cart],
            "total": total_price
        }
        customer.past_orders.append(order)
        customer.cart.clear()
        print(f"✅ สั่งซื้อสำเร็จ! รหัสคำสั่งซื้อ: {order_id}")
        return order_id

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print("📦 รายละเอียดคำสั่งซื้อ:")
                print(f"รหัส: {order['order_id']}")
                for item in order["items"]:
                    print(f"- {item[0]}: {item[1]} ชิ้น")
                print(f"💰 รวมทั้งหมด: {order['total']} บาท")
                return
        print("❌ ไม่พบคำสั่งซื้อที่ระบุ")

shop = OnlineShop("hair bright", "www.hairbright.com")

product_data = [
    ("Shampoo", "แชมพูสูตรอ่อนโยน", 199),
    ("Hair Conditioner", "ครีมนวดผมบำรุงล้ำลึก", 199),
    ("Hair Scissors", "กรรไกรตัดผมคุณภาพสูง", 159),
    ("Clippers", "เครื่องตัดผมไฟฟ้า", 125),
    ("Combs and Brushes", "หวีและแปรงผม", 200),
    ("Products for coloring, straightening, and curling", "ผลิตภัณฑ์สำหรับทำสี ยืด และดัดผม", 299),
    ("Hair treatment and mask", "ทรีตเมนต์และมาสก์บำรุงผม", 209),
    ("Hair serum and oil", "เซรั่มและน้ำมันบำรุงผม", 189)
]

for name, desc, price in product_data:
    product = Product(name, desc, price, shop)
    shop.products.append(product)

customer = Customer("mummum", "mummum@hothot.com", "1/1 m.1 nakhonpathom")

shop.addingItemsToCart(customer, shop.products[0], 2)  # Shampoo x2
shop.addingItemsToCart(customer, shop.products[7], 1)  # Hair serum and oil x1

order_id = shop.checkOut(customer)

shop.orderTracking(customer, order_id)