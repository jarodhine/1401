def Menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def Main():
    user_name = str(input("Enter name: "))
    Menu()
    user_input = str(input(": "))
    while user_input != "Q":
        if user_input == "H":
            print("Hello ",user_name)
            user_input = []
        elif user_input == "G":
            print("Goodbye ",user_name)
            user_input = []
        else:
            print("Invalid choice")
            user_input = []
        Menu()
        user_input = str(input(": "))
Main()
