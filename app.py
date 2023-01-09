import numpy as np
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template, redirect
from voice_verification import VoiceVerification
from werkzeug.utils import secure_filename
#import speech_recognition as sr
import logging as log
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#model = joblib.load("my_model.pkl")
import os
cwd = os.getcwd()

#@app.route('/voice_verification',methods=['POST'])
@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
          
        if "file" not in request.files and "file2" not in request.files:
            return redirect(request.url)

        file1 = request.files["file"]
        file2 = request.files["file2"]
        file1.save(os.path.join(cwd, file1.filename))
        file2.save(os.path.join(cwd, secure_filename(file2.filename)))
        #print("filename " + file1.filename)
        if file1.filename == "":
            return redirect(request.url)
        if file2.filename == "":
            return redirect(request.url)    

        if file1:
            
            transcript = VoiceVerification(file1.filename, file2.filename)
             
    return render_template('index_upload.html', transcript=transcript)

    



if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5001)
