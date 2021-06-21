import csv
import Get_Score
from Town import Town
import Connection
from Algorithm import algorithm
from Clustering import cluster_data

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
    # Gets all combinations of coordinates, except combinations of itself, and gets Connection info from it
    combos = []
    for i in coordinates:
        for j in coordinates:
            if i != j:
                combos.append([coordinates.index(i), coordinates.index(j), Connection.get_distance(i, j)])
    return combos

def getMinimum(lst,index):
    minimum = 10000000
    for i in lst:
        if i[index] < minimum:
            minimum = i[index]
    return minimum

def getMaximum(lst,index):
    maximum = 0
    for i in lst:
        if i[index] > maximum:
            maximum = i[index]
    return maximum

def evaluate():
    #Oud probleem: al 100 proberen te doen zorgt voor 100! combinaties oftewel 9.33*10^157 combinaties.
    #Nieuw plan: opsplitsen in enorme grid.
    #Beter plan: verminder naar 150 stuks. Gebruik data learning en k-means clustering om te vereenvoudigen.
    coords = get_coordinates(get_data())
    x1 = getMinimum(coords, 0)
    x2 = getMinimum(coords, 1)
    y1 = getMaximum(coords, 0)
    y2 = getMaximum(coords, 1)
    print((y1 - x1)**0.5) #Square root is the most efficient
    print((y2 - x2)**0.5) #197769/(71.4*58.3) = 46.6. #47! = 2.57*10^59
    # dit moet nog meer vermenigvuldigt worden. ik ga alles nog delen door 2,
    # dus intel zal per (72/2 * 58/2) 36x29 pixels gaan. dan per 4 heb ik 4! mogelijkheden. en dat dan steeds uitbreiden.
    # Probleem is dat dijkstra Niet toegepast kan worden
    #
    dijkie = Get_Score.Score(coords=coords)
    state = [0, 4, 2, 3, 1]
    result, route = dijkie.evaluate(state)
    plot_coords(coords,route)
    return result


def plot_coords(coords,route):
    import matplotlib.pyplot as plt
    '''
    Plots all points in a scatterplot
    :returns nothing:
    '''
    x, y = [], []
    for i in get_coordinates(get_data()):
        x.append(i[0]), y.append(i[1])
    plt.scatter(x, y)
    xl, yl = [],[]
    for i in route:
        xl.append(coords[i][0])
        yl.append(coords[i][1])
    plt.plot(xl,yl)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return None

print(cluster_data(get_coordinates(get_data())))