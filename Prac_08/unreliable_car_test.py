from Prac_08.unreliable_car import UnreliableCar

car1 = UnreliableCar("Sedan", 100, 50)
assert car1.name == "Sedan"
assert car1.fuel == 100
assert car1.reliability == 50
car1.drive(50)
print(car1)