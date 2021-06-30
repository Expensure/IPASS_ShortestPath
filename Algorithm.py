"""
Nearest neighbor pseudocode, van https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm:
    1. Start bij de eerste coordinaat uit de dataset O.
    2. Zoek de dichtstbijzijnde coordinaat bij O die N heet.
    3. Als N is gevonden, zet N neer als O en zet de coordinaat van O als "Visited"
    4a. Als elke coordinaat staat onder "Visited", Return de volledige route, beeindig het algoritme
    4b. Zo niet, ga naar stap 2
"""


def calculate_dist(t1, t2):
    # Gebruikt pythagoras om afstand tussen twee towns te berekenen
    x_distance = abs(t1.x - t2.x)
    y_distance = abs(t1.y - t2.y)
    return int(round((x_distance ** 2 + y_distance ** 2)) ** 0.5)


# Schrijft output van de route naar een aparte file
def export_route(filename, tour, distance):
    with open(filename + ".tour", "w") as file:
        file.write(str(distance) + '\n')
        for city in tour:
            file.write("%d\n" % city.id)


def calc_path_dist(route):
    tot = 0
    for idx in range(0, len(route) - 1):
        tot += calculate_dist(route[idx], route[idx + 1])
    tot += calculate_dist(route[len(route) - 1], route[0])

    return tot


def algorithm(selected, route):
    """
    Zoekt naar kortste afstand tussen current punt 'selected' en een ander punt op de route
    """
    min_length = float("inf")
    closest = None
    for i in route:
        if i.id != selected.id:
            distance = calculate_dist(selected, i)
            if min_length > distance:
                closest = i
                min_length = distance

    return closest


def nearest_neighbor(route):
    new_route = []
    current_city = route.pop(0)
    new_route.append(current_city)
    while route:
        newest = algorithm(current_city, route)
        current_city = newest
        route.remove(newest)
        new_route.append(current_city)

    return new_route


"""
2-Opt pseudocode, van https://www.cs.ubc.ca/~hutter/previous-earg/EmpAlgReadingGroup/TSP-JohMcg97.pdf
    two_opt_swap(route, i, k) 
           1. Neem het begin tot punt i en zet hem in new_route
           2. Neem punt i tot en met punt k, draai hem om, en zet hem in new_route
           3. Neem alles na punt k, en zet hem in new_route
    return new_route;

    Wat er dan bijvoorbeeld gebeurt:
    >>> two_opt_swap([1,2,3,4,5,6,7,8,9], i = 4, k = 7)
    - resulteert in 1:[1,2,3], 2:[4,5,6,7], 3: [8,9]
    - draai 2 om, 2:[7,6,5,4]
     - resulteert in [1,2,3,7,6,5,4,8,9]
Dit wordt vervolgens beoordeeld
en als de lengte korter is dan dat het was, wordt het verbeterd.
dit wordt gedaan tot geen verbetering meer voorkomt.

"""


def two_opt_swap(route, i, k):
    new_route = []

    # 1. take route[0] to route[i-1] and add them in order to new_route
    for index in range(0, i):
        new_route.append(route[index])

    # 2. take route[i] to route[k] and add them in reverse order to new_route
    for index in range(k, i - 1, -1):
        new_route.append(route[index])

    # 3. take route[k+1] to end and add them in order to new_route
    for index in range(k + 1, len(route)):
        new_route.append(route[index])

    return new_route


# @profile
def two_opt_solve(s):
    improvement = True
    while improvement:
        improvement = False
        best_distance = calc_path_dist(s)
        i = 1
        while i < len(s):
            for k in range(i + 1, len(s)):
                new_route = two_opt_swap(s, i, k)
                new_distance = calc_path_dist(new_route)
                if new_distance < best_distance:
                    s = new_route
                    best_distance = new_distance
                    improvement = True
                    i = 1
            else:
                i += 1

    return s


def toString(s):
    return "Distance: " + str(calc_path_dist(s))


def run_alg(coordinate_list):
    coordinate_list2 = coordinate_list.copy()
    coordinate_list3 = coordinate_list.copy()
    print(toString(coordinate_list))

    greedy = nearest_neighbor(coordinate_list)

    print("\nRoute na oude algoritme")
    print(toString(greedy))

    result = two_opt_solve(coordinate_list3)

    print("\nNa een aantal 2-opt swaps")
    print(toString(result))
    return result, greedy
