import math

fuel_reqs = []
f = open("input.txt", "r")
massList = [int(i) for i in f.readlines()]

def fuel_need(mass):    
    return math.floor(mass / 3) - 2

def total_fuel_needs(massList):
    for mass in massList:
        total_rf = 0
        req_fuel = fuel_need(mass)
        while req_fuel >= 0:
            total_rf += req_fuel
            req_fuel = fuel_need(req_fuel)        
        fuel_reqs.append(total_rf)
    return sum(fuel_reqs)

print("the sum of the fuel requirements for all of the modules:", total_fuel_needs(massList))