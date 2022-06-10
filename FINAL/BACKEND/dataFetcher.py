import log
import energyCalc
from os.path import exists
from os import listdir

# returns the file name for the corespoding user id

def getFuelType(vehicleModel):
    s = vehicleModel.split('#')
    return s[0]
def getVehicleType(vehicleModel):
    s = vehicleModel.split('#')
    vehicle = s[1]
    vehicle = vehicle.strip('\n')
    return vehicle
    
# returns true if a log file exists for the given user where fileName=userId
def fileExists(userId):
    real = exists(userId+'.txt')
    return real

def userVehicle(userId):
    vm = log.getVehicleModel(userId)
    fuel = getFuelType(vm)
    vehicle = getVehicleType(vm)
    return fuel, vehicle

def createLog(userID, fuelType, vehicleType):
    if(fileExists(userID)):
        return
    with open(userID +'.txt', 'w') as f:
        f.write(fuelType + '#' + vehicleType +'\n')

# Calls a flies in the log.py for the sace of a single point of contact
def addLogEntry(userId, date,odometer,fuel):
    log.newLog(userId,date,odometer,fuel,0)

def getLog(userId, dateStart, dateEnd):
    fuelType = getFuelType(log.getVehicleModel(userId))
    logs = log.getLogsBetweenDates(userId, dateStart, dateEnd)
    return calcaultLogs(logs, fuelType)
    

# returns the total disntance and energy form a list of log items 
def calcaultLogs(logs, fuelType):
    totalDistance = 0
    totalEnergy = 0
    i = 0
    for x in logs:
        totalEnergy += energyCalc.energyUsedOverDistance(x.distance,x.petrol,fuelType)
        totalDistance += x.distance
    if(totalDistance != 0):
        avgEnergy = totalEnergy/totalDistance
        print('good')
    else:
        avgEnergy = 0
        print('bad')
    return totalDistance, totalEnergy, avgEnergy

def vehiclesWithFuelType(fuelType):
    v=[]
    l = listdir()
    for x in l:
        if(x.endswith('.txt') and x != 'users.txt'):
            m = log.getVehicleModel(x[0:len(x)-4])
            s = m.split('#')
            if(s[0] == fuelType):
                v.append(getVehicleType(m))
    return v

def getCombinedLog(fuel, vehicle, dateStart, dateEnd):
    logList = []
    l = listdir()
    for x in l:
        if(x.endswith('.txt') and x != 'users.txt'):
            vm = log.getVehicleModel(x[0:len(x)-4])
            if(getFuelType(vm) == fuel or fuel == 'All'):
                if(getVehicleType(vm)==vehicle or vehicle == 'All'):
                    logList.extend(log.getLogsBetweenDates(x[0:len(x)-4],dateStart,dateEnd))

    return calcaultLogs(logList, fuel)
    