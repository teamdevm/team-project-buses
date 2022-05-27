from flask import Flask
import handlers


app = Flask(__name__)

@app.route("/")
def hello():
    return handlers.hello()

