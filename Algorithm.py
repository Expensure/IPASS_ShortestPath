from itertools import permutations


def algorithm(cities):
    #Finds shortest combination of routes
    path, min_length = calc_length(cities, range(len(cities)))
    min_path = range(len(cities))

    for path in permutations(range(len(cities))):
        path, length = calc_length(cities, path)
        if length < min_length:
            min_length = length
            min_path = path

    return min_path, min_length


def calc_length(cities, path):
    # vereenvoudigde vorm van pythagoras
    def dist_squared(c1, c2):
        t1 = c2[0] - c1[0]
        t2 = c2[1] - c1[1]

        return t1 ** 2 + t2 ** 2

    length = 0
    for i in range(len(path)):
        length += dist_squared(cities[path[i - 1]], cities[path[i]]) ** 0.5

    return path, length

# 3! duurt 0.0s (6 combinaties)-----------------------------------------------------------------------
# 4! duurt 0.0s (24 combinaties)
# 5! duurt 0.0010s (120 combinaties) (* 25 = 0.025s als 5x5 grid voor 125 entries) Lijkt beste optie
# 6! duurt 0.0030s  (720 combinaties)
# 7! duurt 0.022s  (5040 combinaties)
# 8! duurt 0.210s (40k combinaties)------------------------------------------------------------------
# 9! duurt 2.091s (363k combinaties)
