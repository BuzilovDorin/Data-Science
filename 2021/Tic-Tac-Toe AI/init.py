# Using flask for simple webhook initialization in order to run our webpage.
# Not necessary to use django as much of what django can do, flask can do in a more lightweight way
from flask import Flask, redirect, url_for, render_template, request, jsonify
from static.Backend.algorithm import coinToss, AiTurn, checkWin
from flask_cors import CORS, cross_origin
import os
import json

# Global Variables
# True = Player Max (first move)
# False = AI Max (first move)
maxMin = True

# Declaring the app
app = Flask(__name__)
cors = CORS(app)


# Render homepage
@app.route("/")
def main():
    return render_template('index.html')


# Route for CoinToss
@app.route("/coinToss", methods=["POST"])
def toss():
    if request.method == "POST":
        incomDATA = request.data
        s = int(''.join(filter(str.isdigit, str(incomDATA))))
        v = coinToss(s)
        global maxMin
        maxMin = v
        return jsonify(v)


# Route for AI Next Move
@app.route("/AITurn", methods=["POST"])
def logic():
    if request.method == "POST":
        # Unpacking incoming data == current board state
        decodedData = (request.data).decode('utf-8')
        obj = json.loads(decodedData)
        currGrid = [*obj.values()][:9]
        # Passing through the current board state to the backend AI logic
        a = AiTurn(currGrid)
        return jsonify(a)


# Check if win condition satisfied afer AI has made its move
@app.route("/winCond", methods=["POST"])
def winCon():
    if request.method == "POST":
        decodedData = (request.data).decode('utf-8')
        obj = json.loads(decodedData)
        curGrid = [*obj.values()][:9]
        wCon = checkWin(curGrid)
        return jsonify(wCon)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
