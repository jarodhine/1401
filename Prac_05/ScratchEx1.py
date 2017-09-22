import operator

UserString = str(input("Enter string: "))
Words = UserString.split()
SortedWords = sorted(Words, key=operator.itemgetter(0))
counts = dict()

for word in SortedWords:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

Width = max([len(s) for s in Words])


for key, value in counts.items():
    print("{0:{2}} = {1}".format(key, value, Width))