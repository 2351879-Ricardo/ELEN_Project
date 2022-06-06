from crypt import methods
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

<strong>
cors = CORS(app)

@app.route('./reciever', methods=['POST'])
def postME():
    data = request.get_json()
    data= jsonify(data)
    return data
@app.route('./test', methods=['GET'])
def test():
    return 'bingo'

if(__name__ == "__main__"):
    app.run()