import requests
from flask import Flask
import django
import urllib3

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Dependency Guardian Test",
        "status": "running"
    }

if __name__ == "__main__":
    app.run(debug=False)