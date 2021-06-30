import matplotlib.pyplot as plt
from Clustering import cluster_main
from Algorithm import run_alg
from Town import Clustered_Town
from tools import *




def create_clustered_towns(clusters):
    x = 0
    clustered_towns = []
    for i in clusters:
        index = clusters.index(i)
        cluster = []
        for j in i:

            num_array = []
            for num in j:
                num_array.append(int(float(num)))
            cluster.append(Clustered_Town(x, num_array[0], num_array[1], index))
            x += 1
        clustered_towns.append(cluster)
    return clustered_towns


def test_main():
    data = import_file("cities_100.csv")
    coord_data = get_coords_of_towns(data)
    clusters = cluster_main(coord_data, 2)
    towns = create_clustered_towns(clusters)
    two_time, _ = run_alg(data)
    plot_lines(get_coords_of_towns(two_time))
    plt.show()
    plot_lines(get_coords_of_towns(two_time))
    for i in towns:
        two_opt, _ = run_alg(i)
        plot_lines(get_coords_of_towns(two_opt))
    plt.show()


def new_main():
    data = import_file("cities_subset150.csv")
    plot_base(get_coords_of_towns(data))
    plt.show()
    plot_lines(get_coords_of_towns(data))
    plt.show()

    two_opt, nearest_neighbours = run_alg(data)

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


# def main():
# data = import_file("cities_subset150.csv")
# clustered = cluster_main(data)
# total = []
# for i in clustered:
# starts, ends = [], []
# cluster = []
# for j in i:
# path,time = algorithm(j)
# cluster.append(total)
# plot_coords(j,path)
# starts.append(j[path[0]])
# ends.append(j[path[len(path)-1]])
# plt.show()
# total.append(cluster)
# plot_tussen(connections)
# plt.show()

new_main()
