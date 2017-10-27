from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

cars =  [SilverServiceTaxi("Limo", 100, 3), Taxi("Prius", 90), SilverServiceTaxi("Hummer", 200, 2)]
keyinput = ""
bill = 0
tripbill = 0

print("Let's Drive!")
while keyinput != "q":
    print("q)uit c)hoose taxi, d)rive")
    keyinput = input()
    if keyinput == "c":
        for c, car in enumerate(cars):
            print(c, car)
        taxi = int(input("Choose taxi: "))
        bill += float(cars[taxi].get_fare())
        print("Bill to date: ${:,.2f}".format(bill))
    if keyinput == "d":
        distance = int(input("Drive how far: "))
        cars[taxi].drive(distance)
        tripbill = float(cars[taxi].get_fare())
        bill += float(cars[taxi].get_fare())
        print("Your {} trip cost you: ${:,.2f}".format(cars[taxi].name, tripbill))
        print("Bill to date: ${:,.2f}".format(bill))

print("Total trip cost: ${:,.2f}".format(bill))
print("Taxis are now:")
for c, car in enumerate(cars):
    print(c, car)
