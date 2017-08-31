def Menu():
    print("(1) Show the even numbers from x to y")
    print("(2) Show the odd numbers from x to y")
    print("(3) Show the squares from x to y")
    print("(4) Exit the program")

def Main():
    user_x = int(input("Enter X: "))
    user_y = int(input("Enter Y: "))
    Menu()
    user_input = int(input(": "))
    while user_input != 4:
        if user_input == 1:
            for i in range(user_x, user_y):
                if i%2 == 0:
                    print(i, end=' ')
            print()
        elif user_input == 2:
            for i in range(user_x, user_y):
                if i%2 != 0:
                    print(i, end=' ')
            print()
        elif user_input == 3:
            for i in range(user_x, user_y):
                print((i**2), end=' ')
            print()
        else:
            print()
        Menu()
        user_input = int(input(": "))
Main()
