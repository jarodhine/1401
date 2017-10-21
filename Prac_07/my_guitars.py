from Prac_07.guitar import Guitar

print("My guitars!")

guitars = []

name = 'defaul'

while name is not '':
    name = input("Name: ")
    if name is not '':
        year = input("Year: ")
        cost = int(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${:,.2f} added.".format(name, year, cost))


for x, i in enumerate(guitars):
    if i.is_vintage == True:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} (vintage)".format(x, i.name, i.year, i.cost))
    else:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(x, i.name, i.year, i.cost))
