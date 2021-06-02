import random
import os
from flask import Flask, request, jsonify, render_template
import requests
from predict import prediction

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    file_name = "abc.wav"
    raw_data = request.get_data()
    f = open(file_name, "wb")
    f.write(raw_data)
    f.close()
    predicted_keyword = prediction(file_name)
    os.remove(file_name)
    result = {"keyword": predicted_keyword}
    return jsonify(result)

@app.route('/', methods=["GET"])
def index():
    return "<h1>Welcome to the server!</h1>"

if __name__ == "__main__":
    app.run(debug=False)