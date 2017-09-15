def main():
    score = GetScore()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def GetScore():
    score = float(input("Enter score: "))
    return score

main()