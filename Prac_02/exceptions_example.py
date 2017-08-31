"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? : When the entered values are not a number
2. When will a ZeroDivisionError occur? : When the denominator value is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? : Yes, loop until user enters a vlue higher than 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("0 is not valid please try again")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")