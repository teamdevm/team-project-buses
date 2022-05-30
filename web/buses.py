import http.client

from flask import Flask, request
import handlers
# TODO: add middleware to catch db exceptions

app = Flask(__name__)


@app.route("/")
@app.route("/login", methods=["GET"])
def login_page():
    return handlers.login_page()


@app.route("/login", methods=["POST"])
def login_user():
    if all(field in request.form for field in ["login", "password"]):
        return handlers.login_user(request.form["login"], request.form["password"])
    else:
        return "", http.client.BAD_REQUEST


@app.route("/registration", methods=["GET"])
def registration_page():
    return handlers.registration_page()


@app.route("/registration", methods=["POST"])
def registrate_user():
    if all(field in request.form for field in ["login", "password", "rep_password"]):
        return handlers.registrate_user(
            request.form["login"],
            request.form["password"],
            request.form["rep_password"]
        )
    else:
        return "", http.client.BAD_REQUEST
