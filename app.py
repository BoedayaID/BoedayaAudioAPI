import random
import os
from flask import Flask, request, jsonify, render_template
import requests
from keyword_spotting_service import Keyword_Spotting_Service

# instantiate flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():

    # audio_file = request.files['file']
    # file = open(audio_file.filename, "rb")
    # values = {"file": (audio_file.filename, file, "audio/wav")}

    file_name = "abc"
    raw_data = request.get_data()
    f = open(file_name, "wb")
    f.write(raw_data)
    f.close()

    # get file from POST request and save it
    # audio_file = request.files["file"]
    # file_name = str(random.randint(0, 100000))
    # audio_file.save(file_name)

    # # instantiate keyword spotting service singleton and get prediction
    kss = Keyword_Spotting_Service()
    predicted_keyword, accuracy = kss.predict(file_name)

    # # we don't need the audio file any more - let's delete it!
    os.remove(file_name)

    # # send back result as a json file
    result = {"keyword": predicted_keyword}
    return jsonify(result)
    # return render_template("prediction.html", variable=str(audio_file.filename))
    # return "<h1>TEST</h1>"

@app.route('/', methods=["GET", "POST"])
def index():
    raw_data = request.get_data()
    f = open("a.wav", "wb")
    f.write(raw_data)
    f.close()
    # return raw_data
    return "<h1>Welcome to the server!</h1>"

if __name__ == "__main__":
    app.run(debug=False)