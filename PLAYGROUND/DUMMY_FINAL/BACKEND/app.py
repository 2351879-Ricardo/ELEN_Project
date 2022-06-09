
from flask import Flask, request, jsonify
from flask_cors import CORS
import userLogins
import dataFetcher

# Vehicle types - to be edited impoved and updated as needed
FUEL_TYPES = ['Petrol', 'Diesel', 'Electric']
VEHICEL_TYPES = ["SUV", "hatchback","crossover","convertable","sedan","sports car","coupe","minivan","4x4","pickup","truck","motorbike",]

app = Flask(__name__)
cors = CORS(app)

# Login funtions
@app.route('/signup/exists', methods=['POST'])
def UserExists():
    userId = request.get_json()
    exists = userLogins.UserExists(userId)
    response = jsonify(exists)
    return response
@app.route('/signup/create', methods=['POST'])
def CreateAccount():
    accountData = request.get_json()
    id = accountData['userID']
    password = accountData['password']
    userLogins.CreateUser(id,password)
    return jsonify(True)
@app.route('/signin/valid', methods=['POST'])
def CheckValidSignin():
    loginAttempt = request.get_json()
    id = loginAttempt['userID']
    password = loginAttempt['password']
    loginGood = userLogins.IsValidSignIn(id, password)
    return jsonify(loginGood) 
# Log funtions
@app.route('/log/exists', methods=['POST'])
def CheckLogExists():
    userID = request.get_json()
    exists = dataFetcher.fileExists(userID)
    return jsonify(exists)
@app.route('/log/vehicle', methods=['POST'])
def GetUserVehicle():
    userID = request.get_json()
    fuel, vehicle = dataFetcher.userVehicle(userID)
    vehicle = [{'fuel':fuel, 'vehicle':vehicle}]
    return jsonify(vehicle)
@app.route('/log/create', methods=['POST'])
def CreateNewLog():
    logInfo = request.get_json()
    userID = logInfo['userID']
    fuelType=logInfo['fuel']
    vehicleType=logInfo['vehicle']
    dataFetcher.createLog(userID,fuelType,vehicleType)
    return jsonify(True)
@app.route('/log/post', methods=['POST'])
def PostLog():
    logData = request.get_json()
    userID = logData['userID']
    logDate = logData['logDate']
    odometer = logData['odometer']
    averageConsumption = logData['aveFuel']
    dataFetcher.addLogEntry(userID,logDate,float(odometer),float(averageConsumption))
    return jsonify(True)
# Comparison funtions
@app.route('/database/userlog', methods=['POST'])
def GetUserLogs():
    requestData = request.get_json()
    print(requestData)
    userID = requestData['userID']
    dateStart = requestData['dateStart']
    dateEnd = requestData['dateEnd']
    distance, energy, avgEnergy = dataFetcher.getLog(userID, dateStart, dateEnd)
    userData = [{
        'distance':distance,
        'energy':energy,
        'average':avgEnergy,
    }]
    return jsonify(userData)
@app.route('/database/average', methods=['POST'])
def GetCombinedLogs():
    requestData = request.get_json()
    travelDatas = []
    for vehicle in requestData:
        vehicelType = vehicle['vehicle']
        fuelType = vehicle['fuel']
        dateStart = vehicle['dateStart']
        dateEnd = vehicle['dateEnd']
        distance, energy, avgEnergy = dataFetcher.getCombinedLog(fuelType, vehicelType,dateStart, dateEnd)
        travelDatas.append({
            'distance':distance,
            'energy':energy,
            'average':avgEnergy,
        })
    return jsonify(travelDatas)
# Basic get funtions
@app.route('/database/types', methods=['GET'])
def GetBasicTypes():
    typeData = [{'fuel':FUEL_TYPES, 'vehicle':VEHICEL_TYPES}]
    return jsonify(typeData)
@app.route('/database/offueltype', methods=['POST'])
def GetBasicVehcilesWithFuelType():
    Fueltype = request.get_json()
    vehicles = dataFetcher.vehiclesWithFuelType(Fueltype)
    return jsonify(vehicles)

if(__name__ == "__main__"):
    app.run()