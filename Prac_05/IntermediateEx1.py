
COLOURS = {"Colour1": "#000000", "Colour2": "#FF0000", "Colour3": "#00FF00", "Colour4": "#0000FF", "Colour5": "#F00000",
           "Colour6": "#00F000", "Colour7": "#0000F0", "Colour8": "#0F0000", "Colour9": "#000F00", "Colour10": "#00000F"}

for k in COLOURS.keys():
    print(k)

selection = input("Enter Colour: ")

if selection in COLOURS.keys():
    print(COLOURS[selection])
