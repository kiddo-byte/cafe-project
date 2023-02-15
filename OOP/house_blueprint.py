class House():
    def __init__(self, location, owner, price, roof):
        self.location = location
        self.owner = owner
        self.roof = roof
        self.price = price

house_owner_one = House("Westlands", "Precious", "6.5M", "98 pieces")
print(house_owner_one.location)
print(house_owner_one.owner)
print(house_owner_one.price)
print(house_owner_one.roof)

print("------------------End of house_owner_one-----------------------")

house_owner_two = House("Ngara", "Kadish", "7M", "112 pieces")
print(house_owner_two.location)
print(house_owner_two.owner)
print(house_owner_two.price)
print(house_owner_two.roof)

print("------------------End of house_owner_two-----------------------")