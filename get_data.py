import numpy as np
from matplotlib import pyplot as plt
import csv


def get_coords():
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


def plot_coords():
    '''
    Plots all points in a scatterplot
    :returns nothing:
    '''
    x, y = get_coords().T
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return None


plot_coords()
