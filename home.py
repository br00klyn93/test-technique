import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response
import base64
# import GrammarChecker as g
import time
import json
import requests
# from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


LD_LIBRARY_PATH='/app'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def kys():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def main():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = "test.png"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
            
    return render_template("index.html")
