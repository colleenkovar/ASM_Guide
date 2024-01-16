from flask import Flask
import os

os.environ['DD_SERVICE'] = "testing"
os.environ['DD_ENV'] = "prod"
os.environ['DD_LOGS_INJECTION'] = "true"
os.environ['DD_APPSEC_ENABLED'] = "true"

app = Flask(__name__)

@app.route("/")
def index1():
    return "Congratulations, it's a web app!"

@app.route("/test")
def index2():
    return "It's another web app!"

@app.route("/page")
def index3():
    return "lets add another page"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
