import csv
from Town import Town


def import_file(filename):
    '''
    Gets coordinate data and puts them as Town nodes from CSV file
    :return: List of Town objects
    '''
    with open(filename, "r") as myfile:
        reader = csv.reader(myfile)
        next(reader)
        towns = []
        for line in reader:
            num_array = []
            for num in line:
                num_array.append(int(float(num)))
            towns.append(Town(num_array[0], num_array[1], num_array[2]))
    return towns

def get_data():
    '''
    Gets coordinate data from CSV file
    :return: List of lists of coords
    '''
    with open('cities_subset40.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        city_coords = []
        for row in reader:
            city_coords.append([int(float(row[1])), int(float(row[2]))])
        data = city_coords
    return data

# def get_coordinates(data):
# result = []
# for i in data:
# result.append(i)
# print("coordinates acquired")
# return result


def get_distance(coord_1, coord_2):
    # Returns distance between two coordinates using Pythagoras' Equation
    return round(((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2) ** 0.5)


def get_edges(coordinates):
    # Gets all combinations of coordinates, get indices of them, and gets distance between the two.

    combos = []
    for i in coordinates:
        for j in coordinates:
            if i != j:
                combos.append([coordinates.index(i), coordinates.index(j), get_distance(i, j)])
    return combos
