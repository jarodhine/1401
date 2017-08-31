total = 0

itemnum = int(input("Number of items: "))
while itemnum < 0:
    itemnum = int(input("Number of items: "))

for i in range(0, itemnum, 1):
    itemprice = float(input("Price of item: "))
    while itemprice < 0:
        itemprice = float(input("Price of item: "))
    total = total + itemprice

print("${:.2f}".format(total))