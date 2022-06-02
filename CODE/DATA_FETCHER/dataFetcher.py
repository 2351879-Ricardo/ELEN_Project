#version 0.0.1
#Author: K Ngwenya


from energyCalc import *

def fetchEnergy():
    return energyUsed(odometer, prevOdometer, avgConsumption, fuelType)
    
if __name__ == "__main__":
    fetchEnergy()
    print("ma se poes")