
from flask import Flask, request, jsonify
from flask_cors import CORS
from DATA_FETCHER import userLogins

app = Flask(__name__)

cors = CORS(app)

@app.route('/signup/exists', methods=['POST'])
def UserExists():
    userId = request.get_json()
    print('======================= ID ' + userId + '=========================')
    exists = userLogins.UserExists(userId)
    response = jsonify(exists)
    return response
@app.route('/signup/create', methods=['POST'])
def CreateAccount():
    accountData = request.get_json()
    id = accountData['userID']
    password = accountData['password']
    #userLogins.CreateUser(id,password)
    return jsonify(True)
@app.route('/signin/valid', methods=['POST'])
def CheckValidSignin():
    loginAttempt = request.get_json()
    id = loginAttempt['userID']
    password = loginAttempt['password']
    loginGood = userLogins.IsValidSignIn(id, password)
    return jsonify(loginGood) 


if(__name__ == "__main__"):
    app.run()