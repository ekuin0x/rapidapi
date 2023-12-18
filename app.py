from flask import Flask, request, render_template
from rembg import remove
import random
import requests
import pyrebase

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

@app.route("/test", methods = ["POST"])
def test() : 
    if request.method == "POST" :
        url = request.get_json()["url"]
        try : 
            data = requests.get(url).content
        except : 
            return "Invalid image URL"

        image = remove(data)
        fname = str(random.randint(0,9999999)) + ".png"

        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        storage.child(fname).put(image)
        url = storage.child(fname).get_url("")
        return url
        


def index() : 
    return "<h1> HEY, STALKER! </h1>"


@app.route("/ping")
def ping() : 
    return "Server is Live"

if __name__ == "__main__" : 
    app.run(port=5000, debug=False)