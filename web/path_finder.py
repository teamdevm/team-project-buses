from models import BusStop


def direct_route(dep_stop_id: int, arr_stop_id: int):
    """Find direct bus routes between two stops

    :param arr_stop_id: id for arrival stop
    :param dep_stop_id: id for departure stop
    :return: list of bus ids
    """

    buses = BusStop.select(BusStop.bus_id).where(BusStop.stop_id == dep_stop_id)\
            .intersect(BusStop.select(BusStop.bus_id).where(BusStop.stop_id == arr_stop_id))

    return [b.bus_id.number for b in buses]
