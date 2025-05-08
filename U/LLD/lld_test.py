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
    CREDIT_CARD = 1
    DEBIT_CARD = 2
    CASH = 3
    DIGITAL_WALLET = 4

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
    def __init__(self, item_id: int, name: str, price: float, description: str):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self):
        self.items = []
        
    def add_item(self, food_item: FoodItem):
        self.items.append(food_item)
        
    def get_items(self) -> list[FoodItem]:
        return self.items

class Restaurant:
    def __init__(self, restaurant_id: int, name: str, address: str):
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
        
    def get_total_price(self) -> float:
        return self.food_item.price * self.quantity

class Payment:
    def __init__(self, amount: float, method: PaymentMethod):
        self.payment_id = f"PAY-{int(datetime.now().timestamp())}"
        self.amount = amount
        self.method = method
        self.status = PaymentStatus.PENDING
        self.timestamp = datetime.now()
        
    def process_payment(self):
        # Payment processing logic would go here
        self.status = PaymentStatus.COMPLETED
        return self.status == PaymentStatus.COMPLETED

class Delivery:
    def __init__(self, order: 'Order', delivery_address: str):
        self.delivery_id = f"DEL-{int(datetime.now().timestamp())}"
        self.order = order
        self.delivery_address = delivery_address
        self.status = "PENDING"
        self.dispatch_time = None
        self.delivery_time = None
        
    def dispatch(self):
        self.status = "DISPATCHED"
        self.dispatch_time = datetime.now()
        
    def complete_delivery(self):
        self.status = "COMPLETED"
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
        
    def calculate_total(self) -> float:
        return sum(item.get_total_price() for item in self.items)
    
    def add_payment(self, payment_method: PaymentMethod) -> bool:
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
payment_success = order.add_payment(PaymentMethod.CREDIT_CARD)
if payment_success:
    print(f"Order {order.order_id} payment successful. Total: ${order.calculate_total():.2f}")
    
    # Start delivery
    if order.start_delivery():
        print(f"Order {order.order_id} is out for delivery")
        
        # Complete delivery
        order.complete_delivery()
        print(f"Order {order.order_id} has been delivered")





# from datetime import datetime, timedelta
# from enum import Enum

# class VehicleType(Enum):
#     MOTORCYCLE = 1
#     CAR = 2
#     TRUCK = 3
    
# class SpotType(Enum):
#     COMPACT = 1
#     LARGE = 2
#     HANDICAPPED = 3
#     MOTORCYCLE = 4
    
# class GateType(Enum):
#     ENTRY = 1
#     EXIT = 2
    

# class Vehicle:
#     def __init__(self, license_plate, vehicle_type: VehicleType):
#         self.license_plate = license_plate
#         self.vehicle_type = vehicle_type
        

# class ParkingSpot:
#     def __init__(self, spot_id, spot_type: SpotType):
#         self.spot_id = spot_id
#         self.spot_type = spot_type
#         self.is_available = True
#         self.vehicle = None
        
    
#     def isCompatible(self, vehicle: Vehicle):
#         if self.spot_type == SpotType.MOTORCYCLE:
#             return vehicle.vehicle_type == VehicleType.MOTORCYCLE
#         elif self.spot_type == SpotType.COMPACT:
#             return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR]
#         elif self.spot_type == SpotType.LARGE:
#             return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR, VehicleType.TRUCK]
#         elif self.spot_type == SpotType.HANDICAPPED:
#             return True        
#         return False
    
    
#     def assignVehicle(self, vehicle: Vehicle):
#         if self.is_available and self.isCompatible(vehicle):
#             self.vehicle = vehicle
#             self.is_available = False
#             return True        
#         return False
    
    
#     def removeVehicle(self):
#         self.vehicle = None
#         self.is_available = False
        
        
# class Ticket:
#     def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
#         self.vehicle = vehicle
#         self.spot = spot
#         self.ticket_id = f"T-{int(datetime.now().timestamp())}"
#         self.issued_at = datetime.now()

# class ParkingFeeCalculator:
#     @staticmethod
#     def calculateFeee(ticket: Ticket, exit_time=None):
#         if exit_time is None:
#             exit_time = datetime.now()
        
#         time_parked = max(0.5, (exit_time - ticket.issued_at).total_seconds() / 3600)
#         base_rate = 10
        
#         if ticket.vehicle.vehicle_type == VehicleType.MOTORCYCLE:
#             base_rate *= 0.75
#         if ticket.vehicle.vehicle_type == VehicleType.TRUCK:
#             base_rate *= 1.5
        
#         return max(5, round(base_rate * time_parked, 2))
    

# class ParkingFloor:
#     def __init__(self, level):
#         self.level = level
#         self.spots = {}
        
    
#     def addSpot(self, spot_id, spot_type: SpotType):
#         self.spots[spot_id] = ParkingSpot(spot_id, spot_type)
        
    
#     def getAvailableSpots(self, vehicle: Vehicle):
#         return [spot for spot in self.spots.values() if spot.isAvailable and spot.isCompatible(vehicle)]
    
    
# class ParkingLot:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.floors = {}
        
    
#     def addFloor(self, level):
#         self.floors[level] = ParkingFloor(level)
#         return self.floors[level]
    
    
#     def parkVehicle(self, vehicle: Vehicle):
#         for floor in self.floors.values():
#             for spot in floor.getAvailableSpots(vehicle):
#                 if spot.assignVehicle(vehicle):
#                     return Ticket(vehicle, spot)
        
#         return None
    
    
#     def unparkVehivle(self, ticket: Ticket, exit_time=None):
#         ticket.spot.removeVehicle()
#         return ParkingFeeCalculator.calculateFeee(ticket, exit_time)


# class ParkingGate:
#     def __init__(self, gate_id, gate_type: GateType):
#         self.gate_id = gate_id
#         self.gate_type = gate_type
        
        
#     def processEntry(self, vehicle: Vehicle, parking_lot: ParkingLot):
#         return parking_lot.parkVehicle(vehicle)
    
    
#     def processExit(self, ticket: Ticket, parking_lot: ParkingLot, exit_time=None):
#         return parking_lot.unparkVehivle(ticket, exit_time)    
        



# class FileSystemNode:
#     def __init__(self):
#         self.is_file = False
#         self.children = {}
#         self.content = ''
        

# class FileSystem:
#     def __init__(self):
#         self.root = FileSystemNode()
    
    
#     def _traverse(self, path, create=False, make_file=False):
#         curr = self.root
#         if path == '/':
#             return curr
        
#         parts = path.strip('/').split('/')
#         for _, part in enumerate(parts):
#             if part not in curr.children:
#                 if not create:
#                     raise ValueError(f'Path {path} does not exist')
#                 curr.children[part] = FileSystemNode()
#             curr = curr.children[part]
        
#         if make_file:
#             curr.is_file = True

#         return curr
    
    
#     def ls(self, path):
#         curr = self._traverse(path)
#         if curr.is_file:
#             return [path.split('/')[-1]]
#         return sorted(curr.children.keys())
    
    
#     def mkdir(self, path):
#         self._traverse(path, create=True)
        
        
#     def addContentToFile(self, path, content):
#         curr = self._traverse(path, create=True, make_file=True)
#         curr.content += content
        
    
#     def readContentFromFile(self, path):
#         curr = self._traverse(path)
#         if not curr.is_file:
#             raise FileNotFoundError(f"Path {path} not a file")
#         return curr.content
    
    
#     def delete(self, path):
#         if path == '/':
#             raise ValueError('Cannot delete the root directory!')
        
#         parts = path.strip('/').split('/')
#         *dirs, target = parts
        
#         parent = self._traverse('/' + '/'.join(dirs))
#         if parent is None or target not in parent.children:
#             return FileNotFoundError(f"Path '{path}' does not exist")
        
#         del parent.children[target]
    
    
# fs = FileSystem()
# fs.mkdir("/a/b/c")
# fs.addContentToFile("/a/b/c/d", "hello")
# print(fs.ls("/"))           # ['a']
# print(fs.ls("/a/b/c"))      # ['d']
# print(fs.readContentFromFile("/a/b/c/d"))  # 'hello'
        
    
    