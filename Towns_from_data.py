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
        data = city_coords
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
            if i != j:
                combos.append([coordinates.index(i),coordinates.index(j),Connection.get_distance(i, j)])
    return combos

def evaluate():
    coords = get_coordinates(get_data())
    distances = get_edges(coords)
    dijkie = Dijkstra.TravellingSales(coords=coords)
    state =[1, 3, 4, 2, 0]
    print(dijkie.evaluate(state))
    #TODO
    distances2 = Dijkstra.TravellingSales(distances=list(distances))
    result = distances2.evaluate(state)
    return result

print(evaluate())