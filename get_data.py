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
            towns.append(Town(numArray[0], numArray[1], numArray[2]))
    return towns



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
