from datetime import datetime, timedelta
from enum import Enum

class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3
    
class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3
    HANDICAPPED = 4
    
class GateType(Enum):
    ENTRY = 1
    EXIT = 2
    
    
class Vehicle:
    def __init__(self, license_plate, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        
        
class ParkingSpot:
    def __init__(self, spot_id, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_available = True
        self.vehicle = None
        
    def is_compatible(self, vehicle: Vehicle):
        if self.spot_type == SpotType.MOTORCYCLE:
            return vehicle.vehicle_type == VehicleType.MOTORCYCLE
        elif self.spot_type == SpotType.COMPACT:
            return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR]
        elif self.spot_type == SpotType.LARGE:
            return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR, VehicleType.TRUCK]
        elif self.spot_type == SpotType.HANDICAPPED:
            return True
        
        return False
    
    def assign_vehicle(self, vehicle: Vehicle):
        if self.is_available and self.is_compatible(vehicle):
            self.vehicle = vehicle
            self.is_available = False
            return True
        
        return False
    
    def remove_vehicle(self):
        self.vehicle = None
        self.is_available = True
        
        
class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticked_id = f'T-{int(datetime.now().timestamp())}'
        self.vehicle = vehicle
        self.spot = spot
        self.issued_at = datetime.now()
        
class ParkingFeeCalculator:
    @staticmethod
    def calculate_fee(ticket: Ticket, exit_time=None):
        if exit_time is None:
            exit_time = datetime.now()
            
        time_parked = max(0.5, (exit_time - ticket.issued_at).total_seconds() / 3600)
        
        base_rate = 10
        
        if ticket.vehicle.vehicle_type == VehicleType.TRUCK:
            base_rate *= 1.5
            
        return max(5, round(base_rate * time_parked, 2))
            
            
class ParkinFloor:
    def __init__(self, level):
        self.level = level
        self.spots = {}
        
    def add_spot(self, spot_id, spot_type: SpotType):
        self.spots[spot_id] = ParkingSpot(spot_id, spot_type)
        
    def get_available_spots(self, vehicle: Vehicle):
        return [spot for spot in self.spots.values() if spot.is_available and spot.is_compatible(vehicle)]
    
    
class ParkingLot:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.floors = {}
     
    def add_floor(self, level):
        self.floors[level] = ParkinFloor(level)
        return self.floors[level]
    
    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors.values():
            for spot in floor.get_available_spots(vehicle):
                if spot.assign_vehicle(vehicle):
                    return Ticket(vehicle, spot)
        
        return None
    
    def unpark_vehicle(self, ticket: Ticket, exit_time=None):
        ticket.spot.remove_vehicle()
        
        return ParkingFeeCalculator.calculate_fee(ticket, exit_time)
    
    
class ParkingGate:
    def __init__(self, gate_id, gate_type: GateType):
        self.gate_id = gate_id
        self.gate_type = gate_type
        
    def process_entry(self, vehicle: Vehicle, parking_lot: ParkingLot):
        return parking_lot.park_vehicle(vehicle)
    
    def process_exit(self, ticket: Ticket, parking_lot: ParkingLot, exit_time=None):
        return parking_lot.unpark_vehicle(ticket, exit_time)
        
           
# Example Usage 
# Create parking lot
parking_lot = ParkingLot('Uber Parking Lot', '12345, Lincoln drive, CA, USA.')

# Add floors to the parking lot
floor1 = parking_lot.add_floor(level=1)
floor2 = parking_lot.add_floor(level=2)

# Add spots to the floor
floor1.add_spot(spot_id=101, spot_type=SpotType.COMPACT)
floor1.add_spot(spot_id=102, spot_type=SpotType.LARGE)
floor2.add_spot(spot_id=201, spot_type=SpotType.MOTORCYCLE)
floor2.add_spot(spot_id=202, spot_type=SpotType.HANDICAPPED)

# Create vehicles
car = Vehicle(license_plate="CAR123", vehicle_type=VehicleType.CAR)
truck = Vehicle(license_plate="TRUCK456", vehicle_type=VehicleType.TRUCK)
motorcycle = Vehicle(license_plate="MOTO789", vehicle_type=VehicleType.MOTORCYCLE)

# Create parking gates
entry_gate = ParkingGate(gate_id=1, gate_type=GateType.ENTRY)
exit_gate = ParkingGate(gate_id=2, gate_type=GateType.EXIT)

# Park vehicles
ticket1 = entry_gate.process_entry(car, parking_lot)
ticket2 = entry_gate.process_entry(truck, parking_lot)
ticket3 = entry_gate.process_entry(motorcycle, parking_lot)

# For demonstration, we'll simulate that vehicles were parked for 30 minutes (0.5 hours)
exit_time = datetime.now() + timedelta(minutes=30)

# Unpark vehicles and calculate fees
fee1 = exit_gate.process_exit(ticket1, parking_lot)
fee2 = exit_gate.process_exit(ticket2, parking_lot)
fee3 = exit_gate.process_exit(ticket3, parking_lot)


# Output
print(f'Car packed at spot {ticket1.spot.spot_id}. Fee: ${fee1}')
print(f'Truck packed at spot {ticket2.spot.spot_id}. Fee: ${fee2}')
print(f'Motorcycle packed at spot {ticket3.spot.spot_id}. Fee: ${fee3}')