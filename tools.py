from Town import Town
from get_data import import_file
import matplotlib.pyplot as plt


def get_data_of_sublist(lst, data):
    '''
    Moved from clustering
    Gets coordinates of list of indices
    :param lst: List of indices belonging to sublist
    :param data: Actual coordinates (sublist)
    :return: list of coords belonging to indices
    '''
    total = []
    for i in lst:
        new = []
        for j in i:
            new.append(list(data[j]))
        total.append(new)
    return total

def get_coords_of_towns(lst):
    newlst = []
    for i in lst:
        newlst.append(Town.get_coords(i))
    return newlst

def rotate(list, goal,k = 1,):
    '''
    Rotates list until goal is on the first index
    :param list: list that includes goal
    :param goal: item that needs to be on first index
    :param k: Amount of switches that are done at a time
    :return:
    '''
    while list[0] != goal:
        list = list[k:]+list[:k]
    return list

def evaluate():
    '''Deprecated, may be used later'''

    def getMinimum(lst, index):
        minimum = 10000000
        for i in lst:
            if i[index] < minimum:
                minimum = i[index]
        return minimum

    def getMaximum(lst, index):
        maximum = 0
        for i in lst:
            if i[index] > maximum:
                maximum = i[index]
        return maximum

    # Oud probleem: al 100 proberen te doen zorgt voor 100! combinaties oftewel 9.33*10^157 combinaties.
    # Nieuw plan: opsplitsen in enorme grid.
    # Beter plan: verminder naar 150 stuks. Gebruik data learning en k-means clustering om te vereenvoudigen.
    coords = import_file("No")
    x1 = getMinimum(coords, 0)
    x2 = getMinimum(coords, 1)
    y1 = getMaximum(coords, 0)
    y2 = getMaximum(coords, 1)
    print((y1 - x1) ** 0.5)  # Square root is the most efficient
    print((y2 - x2) ** 0.5)  # 197769/(71.4*58.3) = 46.6. #47! = 2.57*10^59
    # dit moet nog meer vermenigvuldigt worden. ik ga alles nog delen door 2,
    # dus intel zal per (72/2 * 58/2) 36x29 pixels gaan. dan per 4 heb ik 4! mogelijkheden. en dat dan steeds uitbreiden.
    # Andere oplossing om een aangepaste KMeans vorm toe te passen
    # bron: https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/
    # Probleem is dat dijkstra Niet toegepast kan worden
    # Oplossing was om eigen algoritme te maken.
    ###hypothesis = Get_Score.Score(coords=coords)
    path = [0, 4, 2, 3, 1]
    ###result, route = hypothesis.evaluate(path)
    ###plot_coords(coords, route)
    return None  ###result

def plot_base(coords):
    x, y = [], []
    for i in coords:
        x.append(i[0]), y.append(i[1])
    plt.scatter(x, y)

def plot_lines(route):
    '''
    #Plots all points in a scatterplot
    #:returns nothing:
    #'''
    xl, yl = [], []
    for i in route:
        xl.append(i[0])
        yl.append(i[1])
    plt.plot(xl, yl)
    plt.xlabel('X')
    plt.ylabel('Y')
    return None