import operator

UserString = str(input("Enter string: "))
Words = UserString.split()
SortedWords = sorted(Words, key=operator.itemgetter(0))
Counts = dict()

for word in SortedWords:
    if word in Counts:
        Counts[word] += 1
    else:
        Counts[word] = 1

Width = max([len(s) for s in Words])


for key, value in Counts.items():
    print("{0:{2}} = {1}".format(key, value, Width))