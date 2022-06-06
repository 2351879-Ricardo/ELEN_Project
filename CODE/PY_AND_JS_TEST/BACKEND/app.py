
from flask import Flask, request, jsonify
from flask_cors import CORS
import pullTest


app = Flask(__name__)

cors = CORS(app)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()


    response = test(data)


    response = jsonify(response)
    return response


if(__name__ == "__main__"):
    app.run()