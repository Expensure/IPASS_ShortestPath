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


def algorithm_connect(start_coords, end_coords):
    def get_shortest(lst, coordinate):
        # Vindt het dichtsbijzijnde uiteinde
        shortest = "null"
        minimum = 1000000
        for i in range(len(lst) - 1):
            att = calc_length_two(start_coords[i], coordinate)
            if att < minimum:
                shortest = start_coords[i]
        return [shortest, coordinate], shortest

    def find_index(lst, coordinates):
        # Vindt de index van een item in een ingewikkelde list
        for i in lst:
            if i == coordinates:
                return lst.index(i)

    def set_furthest():
        '''
        Zoekt de twee verste uiteinden tussen gevonden clusters
        :return: indices van de uiteinden
        '''
        startmax, start_index = "null", "null"
        endmax, end_index = "null", "null"
        maximum = 0
        for i in start_coords:
            for j in end_coords:
                att = calc_length_two(i, j)
                if att > maximum:
                    maximum = att
                    startmax, start_index = i, start_coords.index(i)
                    endmax, end_index = j, end_coords.index(j)
        return start_index, end_index

    def calc_closest(starter):
        '''
        Berekent de kortste route tussen
        andere uiteinde van start/eind en een volgend punt
        [start[0]] [--> start here --> end[0], start[1]] [end[1], start[2]] [end[2]]
        meer uitleg in bestand
        '''
        end = end_coords[starter]
        connection, ended = get_shortest(unusedlstend, end)
        return connection, ended

    usedlststart = []
    unusedlstend = end_coords
    start, end = set_furthest()

    usedlststart.append(start)
    routes = []
    while len(unusedlstend) != 1:
        unusedlstend.pop(start)
        conn, ended = calc_closest(start)
        usedlststart.append(find_index(start_coords, ended))
        routes.append(conn)
        start = find_index(start_coords, ended)
    routes.pop(-1)
    return routes


def calc_length_two(coord_1, coord_2):
    # Returnt afstand tussen twee coordinaten
    return round(((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2) ** 0.5)


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

# 3! duurt 0.0s (6 combinaties)
# 4! duurt 0.0s (24 combinaties)
# 5! duurt 0.0010s (120 combinaties) (* 25 = 0.025s als 5x5 grid voor 125 entries) Lijkt beste optie
# 6! duurt 0.0030s  (720 combinaties)
# 7! duurt 0.022s  (5040 combinaties)
# 8! duurt 0.210s (40k combinaties)
# 9! duurt 2.091s (363k combinaties)
