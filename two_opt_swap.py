"""
Nearest neighbor psuedocode, used for the first list, from https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm:
    1. start on an arbitrary vertex as current vertex.
    2. find out the shortest edge connecting current vertex and an unvisited vertex V.
    3. set current vertex to V.
    4. mark V as visited.
    5. if all the vertices in domain are visited, then terminate.
    6. Go to step 2.


2-Opt psuedocode, from https://en.wikipedia.org/wiki/2-opt:
    2optSwap(route, i, k) {
           1. take route[0] to route[i-1] and add them in order to new_route
           2. take route[i] to route[k] and add them in reverse order to new_route
           3. take route[k+1] to end and add them in order to new_route
           return new_route;
       }

    repeat until no improvement is made {
           start_again:
           best_distance = calculateTotalDistance(existing_route)
           for (i = 1; i < number of nodes eligible to be swapped - 1; i++) {
               for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
                   new_route = 2optSwap(existing_route, i, k)
                   new_distance = calculateTotalDistance(new_route)
                   if (new_distance < best_distance) {
                       existing_route = new_route
                       goto start_again
                   }
               }
           }
       }
"""

def calculate_dist(t1, t2):
    x_distance = abs(t1.x - t2.x)
    y_distance = abs(t1.y - t2.y)

    return int(round((x_distance**2 + y_distance**2))**0.5)

# Writes output to file named after the original import file with .tour appended
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


# 1. start on an arbitrary vertex as current vertex.
# 2. find out the shortest edge connecting current vertex and an unvisited vertex V.
# 3. set current vertex to V.
# 4. mark V as visited.
# 5. if all the vertices in domain are visited, then terminate.
# 6. Go to step 2


def algorithm(selected, route):
    #In plaats van 100! combinaties door te gaan, gaat ie nu 100+99+98+97+... combinaties door. Veel minder
    min_length = float("inf")
    closest = None
    for i in route:
        if i.id != selected.id:
            distance = calculate_dist(selected, i)
            if min_length > distance:
                closest = i
                min_length = distance

    return closest


# @profile
def nearest_neighbor(route):
    new_route = []
    current_city = route.pop(0)
    new_route.append(current_city)
    while route != []:
        next = algorithm(current_city, route)
        current_city = next
        route.remove(next)
        new_route.append(current_city)

    return new_route


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
    return"Distance: " + str(calc_path_dist(s))


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
    return result,greedy