from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() : 
    return "Hello World"

@app.route("/ping")
def ping() : 
    return "Server is Live"


if __name__ == "__main__" : 
    app.run(port=5000, debug=False)