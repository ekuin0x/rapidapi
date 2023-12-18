from flask import Flask, request, render_template
import newspaper
import json

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

@app.route("/extract", methods = ["GET"])
def test() : 
    url = request.args.get("url")
    try : 
        article = newspaper.Article(url=url, language='en')
        article.download()
        article.parse()

        title = article.title 
        text = article.text 
        img = article.top_image
        publish_date = datetime.now().strftime("%b-%d, %Y")

        data = {
            "title" : title,
            "text" : text,
            "image" : img,
            "publish_date" : publish_date 
        }
return json.dumps(data)
    except : 
        return "Error occured with provided url"
        
def index() : 
    return "<h1> HEY, STALKER! </h1>"


@app.route("/ping")
def ping() : 
    return "Server is Live"

if __name__ == "__main__" : 
    app.run(port=5000, debug=False)