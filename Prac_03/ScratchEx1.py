def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(ConvertToF(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(ConvertToC(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def ConvertToF(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
def ConvertToC(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()
