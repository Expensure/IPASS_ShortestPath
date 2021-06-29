import matplotlib.pyplot as plt
from get_data import get_data,import_file
from Algorithm import algorithm
from Clustering import cluster_main
from two_opt_swap import run_alg
from Town import Town

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
    return None ###result


def plot_base(coords):
    x, y = [], []
    for i in get_data():
        x.append(i[0]), y.append(i[1])
    plt.scatter(x,y)

def plot_lines(route):
    import matplotlib.pyplot as plt
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

def get_coords_of_towns(lst):
    newlst = []
    for i in lst:
        newlst.append(Town.get_coords(i))
    return newlst

def new_main():
    data = import_file("cities_subset150.csv")
    plot_base(get_coords_of_towns(data))
    plt.show()
    plot_lines(get_coords_of_towns(data))
    plt.show()

    two_opt,nearest_neighbours = run_alg(data)

    plot_base(get_coords_of_towns(data))
    plot_lines(get_coords_of_towns(nearest_neighbours))
    plt.show()

    plot_base(get_coords_of_towns(data))
    plot_lines(get_coords_of_towns(two_opt))
    plt.show()

    plot_base(get_coords_of_towns(data))
    plot_lines(get_coords_of_towns(nearest_neighbours))
    plot_lines(get_coords_of_towns(two_opt))
    plt.show()

#def main():
    #data = import_file("cities_subset150.csv")
    #clustered = cluster_main(data)
    #total = []
    #for i in clustered:
        #starts, ends = [], []
        #cluster = []
        #for j in i:
            #path,time = algorithm(j)
            #cluster.append(total)
            #plot_coords(j,path)
            #starts.append(j[path[0]])
            #ends.append(j[path[len(path)-1]])
        #plt.show()
        #total.append(cluster)
        #plot_tussen(connections)
    #plt.show()
new_main()
