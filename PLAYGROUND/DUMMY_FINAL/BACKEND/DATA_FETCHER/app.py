
from genericpath import exists
from multiprocessing import dummy
from flask import Flask, request, jsonify
from flask_cors import CORS
import userLogins

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
    ## CALL DATA FETCHER FUNCTION [exists = LogExists(userID)]
    exists = False
    return jsonify(exists)
@app.route('/log/vehicle', methods=['POST'])
def GetUserVehicle():
    userID = request.get_json()
    ## CALL DATA FETCHER FUNCTION [vehicle = Uer vehicle]
    vehicle = [{'fuel':'Petrol', 'vehicle':'Truck'}]
    return jsonify(vehicle)
@app.route('/log/create', methods=['POST'])
def CreateNewLog():
    logInfo = request.get_json()
    userID = logInfo['userID']
    fuelType=logInfo['fuel']
    vehicleType=logInfo['vehicle']
    ## CALL DATABASE FUNTION TO MAKE A NEW LOG [CreatLog(userID, fuelType, vehicleType)]
    return jsonify(True)
@app.route('/log/post', methods=['POST'])
def PostLog():
    logData = request.get_json()
    userID = logData['userID']
    logDate = logData['logDate']
    odometer = logData['odometer']
    averageConsumption = logData['aveFuel']
    ## CALL DATABASE FUNTION TO ADD TO THE LOG [ADD LOG(userID, logDate, odometer, averageCOnsumption)]
    return jsonify(True)
# Comparison funtions
@app.route('/database/userlog', methods=['POST'])
def GetUserLogs():
    requestData = request.get_json()
    print(requestData)
    userID = requestData['userID']
    dateStart = requestData['dateStart']
    dateEnd = requestData['dateEnd']

    dummyUser = [{
        'distance':450,
        'energy':2345
    }]
   
    return jsonify(dummyUser)
@app.route('/database/average', methods=['POST'])
def GetCombinedLogs():
    requestData = request.get_json()
    travelDatas = []
    dummyOther = {
        'distance':450,
        'energy':3345
    }
    for vehicle in requestData:
        travelDatas.append(dummyOther)
        vehicelTyoe = vehicle['vehicle']
        fuelType = vehicle['fuel']
        dateStart = vehicle['dateStart']
        dateEnd = vehicle['dateEnd']
    return jsonify(travelDatas)
# Basic get funtions
@app.route('/database/types', methods=['GET'])
def GetBasicTypes():
    typeData = [{'fuel':FUEL_TYPES, 'vehicle':VEHICEL_TYPES}]
    return jsonify(typeData)
@app.route('/database/offueltype', methods=['POST'])
def GetBasicVehcilesWithFuelType():
    type = request.get_json()
    ### Fetch vehilces by type
    return jsonify(VEHICEL_TYPES)

if(__name__ == "__main__"):
    app.run()