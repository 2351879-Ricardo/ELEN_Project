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
    return s[1]
    
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
        f.write(fuelType + '#' + vehicleType)

# Calls a flies in the log.py for the sace of a single point of contact
def addLogEntry(userId, date,odometer,fuel):
    log.newLog(userId,date,odometer,fuel,0)

def getLog(userId, dateStart, dateEnd):
    fuelType = getFuelType(log.getVehicleModel(userId))
    logs = log.getLogsBetweenDates(userId, dateStart, dateEnd)
    return calcaultLogs(logs, fuelType)
    

# returns the total disntance and energy form a list of log items 
def calcaultLogs(logs, fuelType):
    totalDistance = log[-1].odometer = log[0].odometer
    totalEnergy = 0
    i = 0
    prevOdometer= logs[0].odometer
    for x in logs:
        if(i!=0):
            totalEnergy += energyCalc.energyUsed(x.odometer,prevOdometer,fuelType,x.petrol)
        i+=1
    return totalDistance, totalEnergy

def vehiclesWithFuelType(fuelType):
    v=[]
    l = listdir()
    for x in l:
        if(x.endswith('.txt') and x != 'users.txt'):
            m = log.getVehicleModel(x[0:len(x)-4])
            s = m.split('#')
            if(s[0] == fuelType):
                v.append(s[1])
    return v

def getCombinedLog(fuel, vehicle, dateStart, dateEnd):
    logList = []
    l = listdir()
    for x in l:
        if(x.endswith('.txt') and x != 'users.txt'):
            vm = log.getVehicleModel(x[0:len(x)-4])
            if(getFuelType(vm) == fuel or vehicle == 'All'):
                if(getVehicleType(vm)==vehicle or fuel == 'All'):
                    logList.append(log.getLogsBetweenDates(dateStart,dateEnd))
    return calcaultLogs(logList, fuel)
    