def main():
    name = ""
    name = GetName(name)
    SpliceName(name)



def GetName(name):
    name = str(input("Enter name: "))
    while name == "":
        name = str(input("Invalid choice please enter a name: "))
    return name
    
def SpliceName(name):
  print(name[::2])

main()
