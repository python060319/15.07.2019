
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



