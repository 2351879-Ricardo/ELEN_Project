
from flask import Flask, request, jsonify
from flask_cors import CORS
from pullTest import *


app = Flask(__name__)

cors = CORS(app)

@app.route('/test', methods=['POST'])
def test1C():
    data = request.get_json()


    response = test(data)


    response = jsonify(response)
    return response

@app.route('/test2', methods=['POST'])
def test2():
    data = request.get_json()
    id = data['id']
    
    response = jsonify(id)
    return response

if(__name__ == "__main__"):
    app.run()