import random, math

def getHekef(radius):
    return radius * 2 * math.pi

def add(x = 0, y = 0):
    return x + y
def sub(x = 0, y = 0):
    return x - y

def getInRange(min = 10, max = 100):
    #number = int(input("Enter number: "))
    #while number < min or number > max:
    #   number = int(input("Enter number: "))
    #return number
    while True:
        number = int(input(f"Enter number ({min}-{max}): "))
        if number >= min and number <= max:
            return number

print(add(1, 3))

print(getInRange(5, 10))

print(getHekef(6.8))

