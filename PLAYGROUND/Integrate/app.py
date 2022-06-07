
from flask import Flask, request, jsonify
from flask_cors import CORS
#import userLogins

app = Flask(__name__)

cors = CORS(app)

@app.route('/signup/exists', methods=['POST'])
def UserExists():
    userId = request.get_json()
    #exists = userLogins.UserExists(userId)
    exists = (userId == 'fred')
    response = jsonify(exists)
    return response
@app.route('/signup/create', methods=['POST'])
def CreateAccount():
    accountData = request.get_json()
    # --- call make account
    return jsonify(True)
    


if(__name__ == "__main__"):
    app.run()