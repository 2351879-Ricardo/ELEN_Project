from log import *
from os.path import exists
from os import listdir

def fileExists(fileName):
    real = exists(fileName+'.txt')
    return real

def createLog(userID, fuelType, vehicleType):
    if(fileExists(userID)):
        return
    with open(userID + '.txt', 'w') as f:
        f.write(fuelType + '#' + vehicleType)

def getLog(userID, dateStart, dateEnd):
    totalFuel = 0
    totalDistance = 0
    totalEnergy = 0
    logs = getLogsBetweenDates(userID, dateStart, dateEnd)
    for x in logs:
        totalDistance += x.odometer
        totalFuel += x.petrol
    print(totalFuel)
    print(totalDistance)

def vehiclesWithFuelType(fuelType):
    v=[]
    l = listdir()
    for x in l:
        if(x.endswith('.txt') and x != 'users.txt'):
            m = getVehicleModel(x[0:len(x)-4])
            s = m.split('#')
            if(s[0] == 'Diesel'):
                v.append(s[1])
    return v