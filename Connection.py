from collections import namedtuple

Connection = namedtuple('Collection', 'start, end, distance')


def get_distance(coord_1, coord_2):
    # Returns distance between two coordinates using Pythagoras' Equation
    return round(((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2) ** 0.5)


def make_connection(coord_start, coord_end):
    return Connection(coord_start, coord_end, get_distance(coord_start, coord_end))


def get_connection(Connection):
    print(Connection.inspect)
