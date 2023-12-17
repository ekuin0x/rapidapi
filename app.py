from flask import Flask, request, render_template
from rembg import remove
import requests
import pyrebase
import random

config = {
  "apiKey": "AIzaSyBFj4WtVAfarJFy0V6YwccqTNplYajofOo",
  "authDomain": "ytconvert-f92e2.firebaseapp.com",
  "databaseURL": "",
  "storageBucket": "ytconvert-f92e2.appspot.com",
  "appId": "1:479741046984:web:5e86d7729e55b5760ab5fd",
  "measurementId": "G-DSWWEJCHDT"
}

app = Flask(__name__)

@app.route("/")
def index() : 
    return "<h1> HEY, STALKER! </h1>"

@app.route("/ping")
def ping() : 
    return "Server is Live"

@app.route("/remover", methods = ["POST"])
def remover() : 
    if request.method == "POST" :
        url = request.get_json()["url"]
        res = requests.get(url).content
        image = remove(res)

        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        name = str(random.randint(1, 9000000)) + ".png"
        storage.child(name).put(image)
        url = storage.child(name).get_url("")
        return url

if __name__ == "__main__" : 
    app.run(port=5000, debug=False)