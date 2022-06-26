from flask import render_template, redirect, url_for

from peewee import DoesNotExist
import http.client
from bcrypt import gensalt, checkpw, hashpw
from datetime import date
from time import mktime

import models
import path_finder

err_msgs = {
    "pass don't match": "Введённые пароли не совпадают",
    "user exists": "Пользователь с таким именем уже зарегистрирован"
}


def index():
    return render_template("landing.html")


def login_page():
    return render_template("login.html", failure=False)


def login_user(login_data):
    username = login_data["login"][0]
    password = login_data["password"][0]

    try:
        # find by login
        user = models.User.get(models.User.login == username)
        # check password
        if checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return routes_page()
    except DoesNotExist:
        pass

    return render_template("login.html", failure=True), http.client.NOT_FOUND


def registration_page():
    return render_template("register.html", failure=False, reason="")


def registrate_user(reg_data):
    username = reg_data["login"][0]
    password = reg_data["password"][0]
    rep_password = reg_data["rep_password"][0]

    # check if login already is using
    try:
        models.User.get(models.User.login == username)
        return (render_template(
            "register.html", failure=True,
            reason=err_msgs["user exists"]),
                http.client.BAD_REQUEST
        )
    except DoesNotExist:
        pass

    # check if passwords don't match
    if password != rep_password:
        return (
            render_template("register.html", failure=True,
                            reason=err_msgs["pass don't match"]),
            http.client.BAD_REQUEST
        )

    # if all is ok, create new user
    hashed_pass = hashpw(password.encode("utf-8"), gensalt())
    models.User.create(login=username, password=hashed_pass,
                       registration_date=mktime(date.today().timetuple()))

    return routes_page()


def routes_page():
    stops_name = []
    stops = []
    for stop in models.Stop.select():
        if stop.name not in stops_name:
            stops.append((stop.stop_id, stop.name))
            stops_name.append(stop.name)
    return render_template("pick_stops.html", stops=stops)


def find_routes(route_data):
    dep_stop_id = route_data["departure_stop_id"][0]
    arr_stop_id = route_data["arrival_stop_id"][0]
    return render_template("show_found_routes.html",
                           routes=path_finder.direct_route(dep_stop_id,
                                                           arr_stop_id))
