from unitConverter import *

def distanceTravelled(odometer, prevOdometer):          #This function finds the distance travelled between logs
    return (odometer - prevOdometer)                    # by subtracting the current odometer reading from the previous one
                                                        
                                                
    
def energyCalc(distance, avgConsumption):
    return (round((avgConsumption/100) * distance))     #This function multiplies the average fuel consumption by the distance travelled 
                                                        # to get the total fuel used.
                                                        #The avgConsumption is divided by 100 so that it is used in L/Km form and not
                                                        # L/100Km
                                                
def fuelCost(fuelUsed, pricePerLitre):
    return (fuelUsed * pricePerLitre)


def teslaConsumption(distance, tConsumption):
    return (distance * tConsumption)
    

def fuelTypes(fType, litres):
    if fType == "Petrol":
        return lPetrol2kwh(litres)
    elif fType == "petrol":
        return lPetrol2kwh(litres)
    elif fType == "Diesel":
        return lDesel2kwh(litres)
    elif fType == "diesel":
        return lDesel2kwh(litres)
    
    
if __name__ == "__main__":
    testOdo = int(input("Please enter current odometer reading: "))
    testPrevOdo = int(input("Please enter prev odometer reading: "))
    testAvgConsumption = float(input("Enter average consumption: "))
    testFuelType = input("What kind of fuel does your car use? :")
    pricePerLitre = 23.82
    
    dist = distanceTravelled(testOdo, testPrevOdo)
    fuel = energyCalc(dist, testAvgConsumption)
    cost = fuelCost(fuel, pricePerLitre)
    kwh = fuelTypes(testFuelType, fuel)
    tCon = teslaConsumption(dist, 0.119)
    
    print("You used " + str(fuel) + "L of fuel this month")
    print("That is equivalent to " + str(kwh) + "kWh of electricity")
    print("If you had made the same trip in a Tesla Model 3, you would have used " + str(tCon) + "kWh of energy")
    
    
    