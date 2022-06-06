
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()

    response = "YOU STUPID DONKEY!!!!!!"
    if(data=='nice'):
        response = "well done"


    response = jsonify(response)
    return response


if(__name__ == "__main__"):
    app.run()