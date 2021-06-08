import numpy as np
import csv

from Town import Town
from Connection import Connection
from math import sqrt
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
            city_coords.append([float(row[1]), float(row[2])])
        data = np.array(city_coords)
    return data

def get_towns(data):
    result = []
    for town in data:
        newInstance = Town(town)
        result.append(newInstance)
    return result

def get_distance(start,end):
    return sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

def get_combos():
    combos = []
    towns = get_towns(get_data())
    coords = []
    for i in towns:
        coords.append(i.get_coords())
        for j in towns:
            if i != j:
                combo = Connection(i,j)
                combos.append([combo, get_distance(i.get_coords(),j.get_coords())])

    return combos


print(get_combos())