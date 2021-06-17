import csv
from itertools import permutations
from Town import Town
from time import time
from csv import reader

def algorithm(cities):
    path, min_length = calc_length(cities, range(len(cities)))
    min_path = range(len(cities))

    for path in permutations(range(len(cities))):
        path, length = calc_length(cities, path)
        if length < min_length:
            min_length = length
            min_path = path

    return min_path, min_length


def dist_squared(c1, c2):
    t1 = c2[0] - c1[0]
    t2 = c2[1] - c1[1]

    return t1 ** 2 + t2 ** 2


def calc_length(cities, path):
    length = 0
    for i in range(len(path)):
        length += dist_squared(cities[path[i - 1]], cities[path[i]])

    return path, length

def get_data():
    '''
    Gets coordinate data from CSV file
    :return: List of lists of coords
    '''
    with open('cities_subset20.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        city_coords = []
        for row in reader:
            city_coords.append([int(float(row[1])), int(float(row[2]))])
        data = city_coords
    return data

def get_coordinates(data):
    result = []
    for town in data:
        newInstance = Town(town)
        result.append(newInstance.get_coords())
    return result
start = time()
print(algorithm(get_coordinates(get_data())))
print("Time costed: " + str((time() - start)))

# 3! duurt 0.0s (6 combinaties)
# 4! duurt 0.0s (24 combinaties)
# 5! duurt 0.0010s (120 combinaties) (* 25 = 0.025s als 5x5 grid voor 125 entries) Lijkt beste optie
# 6! duurt 0.0030s  (720 combinaties)
# 7! duurt 0.022s  (5040 combinaties)
# 8! duurt 0.210s (40k combinaties)
# 9! duurt 2.091s (363k combinaties)
