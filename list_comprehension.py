
# list comprehension

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
# create a list of all of the upper case letters in  
#   list of words ["hello", "python", "proffesional", "world"]
# create a list of 100 random numbers
# matrix = [[1,2,3], [4,5,6], [7,8,9]
#   create a list of all sub list in position 0
# create a list of even numbers between 1 and 200
# input 5 numbers for the user into a list
# create a list of all of the words which are longer then 2 characters
#   list of words ["ab", "hello", "cd", "python", "proffesional", "world", "ef"]
# create a list of NUMBERS from all of the stringw which represent a number (hint: isdigit)
#   list of words ["123", "ab", "5", "77", "88f", "9"]

