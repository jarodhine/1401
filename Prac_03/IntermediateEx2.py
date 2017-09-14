def main():
    name = GetName()
    print(name)


def GetName():
    name = str(input("Enter name: "))
    while name == ():
        name = str(input("Invalid choice please enter a name: "))
    return name

main()