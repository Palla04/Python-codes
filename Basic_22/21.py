class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    # Method to calculate the fare charge of the vehicle
    def fare(self):
        return self.seating_capacity * 100

# Child class Bus that inherits from Vehicle
class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        # Call the constructor of the parent Vehicle class
        super().__init__(seating_capacity)

    # Override the fare method to add maintenance charge
    def fare(self):
        # Get the base fare using the parent class method
        base_fare = super().fare()
        # Calculate the maintenance charge as 10% of the base fare
        maintenance_charge = base_fare * 0.10
        # Calculate the total fare including the maintenance charge
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage
bus = Bus()
print("Total Bus fare:", bus.fare())  # Output: 5500
