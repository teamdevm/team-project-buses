from peewee import JOIN
from models import Stop, BusStop


def direct_route(dep_stop_id: int, arr_stop_id: int):
    """Find direct bus routes between two stops

    :param arr_stop_id: id for arrival stop
    :param dep_stop_id: id for departure stop
    :return: list of bus ids
    """

    dep_stop_name = Stop.get(Stop.stop_id == dep_stop_id).name
    arr_stop_name = Stop.get(Stop.stop_id == arr_stop_id).name
    buses = BusStop.select(BusStop.bus_id).join(Stop, JOIN.INNER).where(Stop.name == dep_stop_name)\
            .intersect(BusStop.select(BusStop.bus_id).join(Stop, JOIN.INNER).where(Stop.name == arr_stop_name))

    return [b.bus_id.number for b in buses]
