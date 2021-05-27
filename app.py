import random
import os
from flask import Flask, request, jsonify, render_template
import requests
from keyword_spotting_service import Keyword_Spotting_Service

# instantiate flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():

    audio_file = request.files['file']
    # file = open(audio_file.filename, "rb")
    # values = {"file": (audio_file.filename, file, "audio/wav")}


    # # get file from POST request and save it
    # # audio_file = request.files["file"]
    # file_name = str(random.randint(0, 100000))
    # values.save(file_name)

    # # instantiate keyword spotting service singleton and get prediction
    # kss = Keyword_Spotting_Service()
    # predicted_keyword = kss.predict(file_name)

    # # we don't need the audio file any more - let's delete it!
    # os.remove(file_name)

    # # send back result as a json file
    # result = {"keyword": predicted_keyword}
    # return jsonify(result)
    return render_template("prediction.html", variable=str(audio_file.filename))

@app.route('/')
def index():
    return "<h1>Welcome to the server!</h1>"

if __name__ == "__main__":
    app.run(debug=False)
