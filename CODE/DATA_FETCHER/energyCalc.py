# version 0.2.1
# Author: K Ngwenya
# Last endited: J Jandrell (22-05-26)

from unitConverter import *

def distanceTravelled(odometer, prevOdometer):          #This function finds the distance travelled between logs
    return (odometer - prevOdometer)                    # by subtracting the current odometer reading from the previous one
def fuelUsed(distance, avgConsumption):
    return (float(avgConsumption)/float(100)) * float(distance)
# Cuurently depriciated                                                
#def fuelCost(fuelUsed, pricePerLitre):
    #return (fuelUsed * pricePerLitre)
def teslaConsumption(distance, tConsumption):
    return (distance * tConsumption)
def fuelEnergy(fType, litres):
    if fType == "Petrol":
        return lPetrol2kwh(litres)
    elif fType == "petrol":
        return lPetrol2kwh(litres)
    elif fType == "Diesel":
        return lDesel2kwh(litres)
    elif fType == "diesel":
        return lDesel2kwh(litres)
# A single funtion that should do all caluclations contained within the module
def energyUsed(odometer,prevOdometer, avgConsumption, fuelType):
    distance = distanceTravelled(odometer,prevOdometer)
    litres = fuelUsed(distance,avgConsumption)
    return fuelEnergy(fuelType,litres)
    
