from enum import Enum
from datetime import datetime


class OrderStatus(Enum):
    PLACED = 1
    PAID = 2
    OUT_FOR_DELIVERY = 3
    DELIVERED = 4
    
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    FAILED = 3
    
class PaymentMethod(Enum):
    CARD = 1
    CASH = 2
    WALLET = 3
    
class DeliveryStatus(Enum):
    PENDING = 1
    DISPATCHED = 2
    COMPLETED = 3
    

class User:
    def __init__(self, user_id: int, name: str, email: str, phone: str, address: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
    def place_order(self, restaurant: 'Restaurant', items: list['OrderItem']) -> 'Order':
        return Order(user=self, restaurant=restaurant, items=items)
    
    
class FoodItem:
    def __init__(self, item_id: int, name: str, price: int, description: str):
        self.item_id = item_id
        self.name = name 
        self.price = price
        self.description = description
        

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, food_item):
        self.items.append(food_item)
    
    def get_items(self):
        return self.items
        

class Restaurant:
    def __init__(self, restaurant_id: str, name: str, address: str):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.menu = Menu()
        
    def add_to_menu(self, food_item: FoodItem):
        self.menu.add_item(food_item)
    
    
class OrderItem:
    def __init__(self, food_item: FoodItem, quantity: int):
        self.food_item = food_item
        self.quantity = quantity
        
    def get_total_price(self):
        return self.food_item.price * self.quantity
    

class Payment:
    def __init__(self, amount: float, method: str):
        self.payment_id = f"PAY-{int(datetime.now().timestamp())}"
        self.amount = amount
        self.method = method
        self.status = PaymentStatus.PENDING
        self.timestamp = datetime.now()
        
    def process_payment(self):
        self.status = PaymentStatus.COMPLETED
        return self.status == PaymentStatus.COMPLETED
    

class Delivery:
    def __init__(self, order: 'Order', delivery_address: str):
        self.delivery_id = f"DEL-{int(datetime.now().timestamp())}"
        self.order = order
        self.delivery_address = delivery_address
        self.status = DeliveryStatus.PENDING
        self.dispatch_time = None
        self.delivery_time = None
        
    def dispatch(self):
        self.status = DeliveryStatus.DISPATCHED
        self.dispatch_time = datetime.now()
    
    def complete_delivery(self):
        self.status = DeliveryStatus.COMPLETED
        self.delivery_time = datetime.now()
        

class Order:
    def __init__(self, user: User, restaurant: Restaurant, items: list[OrderItem]):
        self.order_id = f"ORD-{int(datetime.now().timestamp())}"
        self.user = user
        self.restaurant = restaurant
        self.items = items
        self.status = OrderStatus.PLACED
        self.created_at = datetime.now()
        self.payment = None
        self.delivery = None
        
    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)
    
    def add_payment(self, payment_method: PaymentMethod):
        self.payment = Payment(self.calculate_total(), payment_method)
        success = self.payment.process_payment()
        if success:
            self.status = OrderStatus.PAID
        return success
    
    def start_delivery(self):
        if self.status == OrderStatus.PAID:
            self.delivery = Delivery(self, self.user.address)
            self.delivery.dispatch()
            self.status = OrderStatus.OUT_FOR_DELIVERY
            return True
        return False
    
    def complete_delivery(self):
        if self.delivery and self.status == OrderStatus.OUT_FOR_DELIVERY:
            self.delivery.complete_delivery()
            self.status = OrderStatus.DELIVERED
            return True
        return False
        
        
# Example Usage
# Create users
user1 = User(1, "John Doe", "john@example.com", "1234567890", "123 Main St")

# Create restaurant and menu
restaurant = Restaurant(1, "Tasty Bites", "456 Food Ave")
pizza = FoodItem(1, "Pizza", 12.99, "Delicious cheese pizza")
burger = FoodItem(2, "Burger", 8.99, "Juicy beef burger")
restaurant.add_to_menu(pizza)
restaurant.add_to_menu(burger)

# Place order
order_items = [
    OrderItem(pizza, 2),
    OrderItem(burger, 1)
]
order = user1.place_order(restaurant, order_items)

# Process payment
payment_success = order.add_payment(PaymentMethod.CARD)
if payment_success:
    print(f"Order {order.order_id} payment successful. Total: ${order.calculate_total():.2f}")
    
    # Start delivery
    if order.start_delivery():
        print(f"Order {order.order_id} is out for delivery")
        
        # Complete delivery
        order.complete_delivery()
        print(f"Order {order.order_id} has been delivered")
    
