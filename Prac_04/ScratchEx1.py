import random

picks = int(input("How many quick picks? "))

MIN = 1
MAX = 45
numlist = []

for i in range(1, picks):
    for i in range(5):
        num = random.randint(MIN, MAX)
        numlist.append(num)
    numlist.sort()
    print(numlist)
    numlist = []
