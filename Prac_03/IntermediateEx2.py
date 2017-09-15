def main():
    frequency = 0
    frequency = GetFrequency(frequency)
    name = ""
    name = GetName(name)
    SpliceName(name,frequency)

def GetFrequency(frequency):
  try:
    frequency = int(input("Enter frequency: "))
  except:
    print("")
  while frequency <= 0:
    try:
      frequency = int(input("Invalid choice please enter frequency: "))
    except:
      print("")
  return frequency

def GetName(name):
  try:
    name = str(input("Enter name: "))
  except:
    print("")
  while name == "":
    try:
      name = str(input("Invalid choice please enter name: "))
    except:
      print("")
  return name
    
def SpliceName(name,frequency):
  print(name[::frequency])

main()
