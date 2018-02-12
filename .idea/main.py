import random

#1. open inputfile
f = open("input.txt")

#2. store contents inside list
myList = []
for line in f:
    line = line.strip('\n')
    myList.append(line)

#3. random number
x = random.randint(0, len(myList) -1)

#4. print destination
print (myList[x])


