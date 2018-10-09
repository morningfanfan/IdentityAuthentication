from flask import Flask
from flask_jwt import JWT
from . import views, auth

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)