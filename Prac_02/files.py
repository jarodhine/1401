
out_file = open("name.txt", 'w')

out_file.write((input("Please enter your name: ")))

out_file.close()

in_file = open("name.txt", 'r')

print("Your name is: ", in_file.readline())

in_file.close

in_file = open("numbers.txt", "r")

total = 0

for line in in_file:
    number = int(line)
    total = number + total
print(total)

in_file.close()