
# list comprehension
import random

listOfWord = ["hello", "python", "proffesional", "world"]
res = []
for word in listOfWord:
    res.append(word[0])
print(res)

# [ <expression> for <arg> in <list> if <condition> ]

res = [word[0] for word in listOfWord if word[0] != 'h']
print(res)
res = [n**2 for n in range(1, 10)]
print(res)
res = [i * j for i in range(1, 4) for j in range(1, 4)]
print(res)


# create a list of all of the last letter in the
#   list of words ["hello", "python", "proffesional", "world"]
print([word[-1] for word in listOfWord])

# create a list of all of the upper case letters in
#   list of words ["hello", "python", "proffesional", "world"]
print([word.upper() for word in listOfWord])

# create a list of 100 random numbers
#   1: 1-10 2:1-11 3: 1-12 ...
print([random.randint(1, 10 + n) for n in range(100)])

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
#   create a list of all sub list in position 0
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print([l1[0] for l1 in matrix])

# create a list of even numbers between 1 and 200
print([n for n in range(1, 200) if n % 2 == 0])

# input 5 numbers for the user into a list
print([int(input("enter a number: ")) for n in range(5)])

# create a list of all of the words which are longer then 2 characters
#   list of words ["ab", "hello", "cd", "python", "proffesional", "world", "ef"]
w1 = ["ab", "hello", "cd", "python", "proffesional", "world", "ef"]
print([word for word in w1 if len(word) > 2])

# create a list of NUMBERS from all of the stringw which represent a number (hint: isdigit)
#   list of words ["123", "ab", "5", "77", "88f", "9"]
w2 = ["123", "ab", "5", "77", "88f", "9"]
print([int(word) for word in w2 if word.isdigit()])

# create a list of numbers divided by 3 from a given list only if it can be divided without
# a reminder: the list - [9, 6, 10, 12, 15, 19, 21]
l3 = [9, 6, 10, 12, 15, 19, 21]
print([n for n in l3 if n % 3 == 0])

# m = [ [8, 3, 100, -2, 15], [7, 10, 5, 2, 102], [-4 -5 -10 -2 1000] ]
#   create a sorted list : [ [-2, 3, 8, 15] , [2, 5 ... ] ... ]
m = [ [8, 3, 100, -2, 15], [7, 10, 5, 2, 102], [-4, -5, -10, -2, 1000] ]
print([sorted(n) for n in m])

