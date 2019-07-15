
# input city name from user
# check if city in keys
#   if yes print population
#   if not print - not exist - ask for pop from user add to dict
#   in while loop till get 'Exit' in city name

popMap = { 'TEL AVIV' : 443939, 'LONDON' : 8825000, 'PARIS' : 0,'TOKYO' : 13929286}
city = input("Enter city name: ")
while city.upper() != 'EXIT':
    if city.upper() in popMap.keys():
        print(popMap[city.upper()])
    else:
        pop = int(input(f"Enter number of citizens of {city}: "))
        popMap[city.upper()] = pop
    city = input("Enter city name: ")


