#!/usr/bin/env python3
"""
    gortrans is a module that provides methods for fetching the data
    from the Perm city transport servers.
"""

import time
import datetime
import requests

API_BASE="http://www.map.gptperm.ru/json/"

def _api_request(endpoint, payload=None, ts=False):
    """Unified REST request method"""
    url = API_BASE + endpoint

    if ts:
        url += ("?_=" if "?" not in url else "&_=") + str(time.time())

    if payload is None:
        resp = requests.get(url)
    else:
        resp = requests.post(url, json=payload)

    # TODO: In exception handling
    if resp.status_code != 200:
        print("Error code: {}", resp.status_code)
        print(resp.text)

    return resp.json()

def _get_date_fmt(date=None):
    """get date in DD.MM.YYYY format
    :date: Datetime date object or none for today
    :returns: string date

    """
    if date is None:
        date = datetime.date.today()

    return date.strftime("%d.%m.%Y")
    

def get_news():
    """Get the gortrans news"""
    return _api_request("news-links", ts=True)["newsLinks"]

def get_route_tree(date=None):
    """Get lists of routes for different types of transport"""
    date = _get_date_fmt(date)
    return _api_request(f"route-types-tree/{date}/", ts=True)

def get_full_route(route, date=None):
    """Get a full list of stops for a specific route"""
    date = _get_date_fmt(date)
    return _api_request(f"full-route/{date}/{route}")
    
def get_bus_locations(routes):
    """Get the current location of all busses on given routes
    Please note to not blast too many routes at once!
    while server can return them, the frontend limists simultaneous
    requests at 5.

    :routes: a list of all routes of intereest
    :returns: all known busses

    """
    rlist = ""
    for val in routes:
        rlist += f"{val}-"
    return _api_request(f"get-moving-autos/{rlist}")["autos"]
    
def get_busstop_timetable(route, busstop, date=None):
    """get a timetable for route on a busstop"""
    date = _get_date_fmt(date)
    return _api_request(f"time-table-h/{date}/{route}/{busstop}")
    
def get_busstop_routes(busstop, date=None):
    """get a timetable for route on a busstop"""
    date = _get_date_fmt(date)
    return _api_request(f"stoppoint-routes/{date}/{busstop}")["routeTypes"]

def get_busstop_arivals(busstop):
    """get a timetable for route on a busstop"""
    return _api_request(f"arrival-times/{busstop}", ts=True)["routeTypes"]

def get_pavlions(ptype="build"):
    """Get all bus stops of the given pavilion type.

    :ptype: Type of the pavilions to return
    :returns: structure with the pavilions

    """
    return _api_request(f"stops-with-pavilions?updateType={ptype}", ts=True)

def main():

    print(get_pavlions()[0])
    print(get_bus_locations([53])[0])

if __name__ == "__main__":
    main()
