import numpy as np
import csv
import Dijkstra
from Town import Town
import Connection
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
            city_coords.append([int(float(row[1])), int(float(row[2]))])
        data = np.array(city_coords)
    return data

def get_towns(data):
    result = []
    for town in data:
        newInstance = Town(town)
        result.append(newInstance)
    return result

def get_coordinates(data):
    result = []
    for town in data:
        newInstance = Town(town)
        result.append(newInstance.get_coords())
    return result

def get_edges(coordinates):
    #Gets all combinations of coordinates, except combinations of itself, and gets Connection info from it
    combos = []
    for i in coordinates:
        for j in coordinates:
            if i.all != j.all:
                combos.append([np.where(coordinates == i),np.where(coordinates == j),Connection.get_distance(i, j)])
    return combos

def evaluate():
    coords = np.array(get_coordinates(get_data()))
    distances = get_edges(coords)
    dijkie = Dijkstra.TravellingSales(coords=coords)
    state = np.array([0, 1, 4, 3, 2])
    dijkie.evaluate(state)
    print(dijkie.evaluate(state))
    distances2 = Dijkstra.TravellingSales(distances=distances)
    distances2.evaluate(state)
    return None

evaluate()