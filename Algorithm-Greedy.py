import numpy as np


def algorithm(cities):
    best_order = []
    best_length = float('inf')

    for i_start, start in enumerate(cities):
        order = [i_start]
        length = 0

        i_next, next, dist = get_closest(start, cities, order)
        length += dist
        order.append(i_next)

        while len(order) < cities.shape[0]:
            i_next, next, dist = get_closest(next, cities, order)
            length += dist
            order.append(i_next)

        # print(order)

        if length < best_length:
            best_length = length
            best_order = order

    return best_order, best_length


def get_closest(city, cities, visited):
    best_distance = float('inf')
    i_closest_city = "None"
    closest_city = "None"
    for i, c in enumerate(cities):

        if i not in visited:
            distance = dist_squared(city, c)

            if distance < best_distance:
                closest_city = c
                i_closest_city = i
                best_distance = distance

    return i_closest_city, closest_city, best_distance


def dist_squared(c1, c2):
    t1 = c2[0] - c1[0]
    t2 = c2[1] - c1[1]

    return t1 ** 2 + t2 ** 2
# 3! duurt 0.0s (6 combinaties)
# 4! duurt 0.0s (24 combinaties)
# 5! duurt 0.0010s (120 combinaties) (* 25 = 0.025s als 5x5 grid voor 125 entries) Lijkt beste optie
# 6! duurt 0.0030s  (720 combinaties)
# 7! duurt 0.022s  (5040 combinaties)
# 8! duurt 0.210s (40k combinaties)
# 9! duurt 2.091s (363k combinaties)