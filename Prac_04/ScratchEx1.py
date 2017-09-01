import random

MIN = 1
MAX = 45

picks = int(input("How many quick picks: "))

numlist = []

for i in range(picks):
    for i in range(5):
        numlist.append(random.randint(MIN,MAX))
    numlist.sort()
    print(numlist)
    numlist = []
