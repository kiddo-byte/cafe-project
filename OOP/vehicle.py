class Vehicle():
    def __init__(self, owner, price, model, color):
        self.owner = owner
        self.price = price
        self.model = model
        self.color = color

vehicle_owner_one = Vehicle("Precious", "6.5M", "Mercedes", "black")
print(vehicle_owner_one.owner)
print(vehicle_owner_one.price)
print(vehicle_owner_one.model)
print(vehicle_owner_one.color)

print("------------------End of vehicle_owner_one-----------------------")

vehicle_owner_two = Vehicle("Kadish", "7M", "Toyota", "white")
print(vehicle_owner_two.owner)
print(vehicle_owner_two.price)
print(vehicle_owner_two.model)
print(vehicle_owner_two.color)

print("------------------End of vehicle_owner_two-----------------------")

