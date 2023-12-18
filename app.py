from flask import Flask, request, render_template
import newspaper
import json


app = Flask(__name__)

@app.route("/")
def index() : 
    return "<h1> HEY, STALKER! </h1>"

@app.route("/extract", methods = ["GET"])
def test() : 
    url = request.args.get("url")
    return url
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