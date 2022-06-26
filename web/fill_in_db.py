import gortrans as gt
from models import Bus, Stop, BusStop


def get_buses_and_stops():
    buses = []
    stops = {}
    buses_stops = []
    for bus in gt.get_buses():
        buses.append({"bus_id": bus["routeId"], "number": bus["routeNumber"]})
        bus_stops = gt.get_rout_stops(bus["routeId"])
        for stop in bus_stops:
            stops[stop["stoppointId"]] = stop["stoppointName"]
            buses_stops.append({
                "bus_id": bus["routeId"],
                "stop_id": stop["stoppointId"]
            })

    Bus.insert_many(buses).execute()
    Stop.insert_many([
        {"stop_id": s_id, "name": s_name} for s_id, s_name in stops.items()
    ]).execute()
    BusStop.insert_many(buses_stops).execute()


Bus.delete().execute()
Stop.delete().execute()
BusStop.delete().execute()

get_buses_and_stops()
