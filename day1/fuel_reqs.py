import math

massList = []
fuel_reqs = []
f = open("input.txt", "r")
inputLines = f.readlines()
for i in inputLines:
    print(i)
    massList.append(int(i))

def fuel_need(mass):    
    return math.floor(mass / 3) - 2

for mass in massList:    
    fuel_reqs.append(fuel_need(mass))
    print("the fuel needed for the mass of each module: ", fuel_need(mass))

print("the sum of the fuel requirements for all of the modules:", sum(fuel_reqs))