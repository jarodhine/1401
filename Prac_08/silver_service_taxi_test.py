from Prac_08.silver_service_taxi import SilverServiceTaxi

car1 = SilverServiceTaxi("Limo", 100, 3)
assert car1.name == "Limo"
assert car1.fuel == 100
car1.drive(50)
assert(car1.get_fare()) == 189
print(car1.get_fare())