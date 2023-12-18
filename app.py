from flask import Flask, request, render_template
import newspaper
import json
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index() : 
    return "<h1> HEY, STALKER! </h1>"

@app.route("/extract", methods = ["GET"])
def test() : 
    url = request.args.get("url")
    lang = request.args.get("lang") 
    try : 
        article = newspaper.Article(url=url, language=lang)
        article.download()
        article.parse()
        title = article.title 
        text = article.text 
        keywords = article.keywords
        img = article.top_image
        publish_date = datetime.now().strftime("%b-%d, %Y")

        data = {
            "url" : url,
            "title" : title,
            "text" : text,
            "top_image" : img,
            "keywords" : keywords,
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