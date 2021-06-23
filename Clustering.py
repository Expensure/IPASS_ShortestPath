import matplotlib.pyplot as plt # Om de clusters te plotten
from sklearn.cluster import KMeans


def split_xy(data):
    dat_x = []
    dat_y = []
    for i in data:
        dat_x.append(i[0])
        dat_y.append(i[1])
    return dat_x, dat_y

def get_indexi(lst, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = lst.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

def get_clusters(cluster_aantal,lst):
    model_kmeans = KMeans(n_clusters=cluster_aantal).fit(lst)
    labels = list(model_kmeans.labels_)
    new = []
    for i in range(cluster_aantal):
        new.append(get_indexi(labels,i))
    return new,labels

def get_coords(lst,data):
    '''
    Gets coordinates of list of indices
    :param list: List of indices belonging to sublist
    :param data: Actual coordinates (sublist)
    :return: list of coords belonging to indices
    '''
    total = []
    for i in lst:
        new = []
        for j in i:
            new.append(data[j])
        total.append(new)
    return total

def cluster_coords_twice(coords,total):
    #Unused since 22nd of June
    def transfer_to_coords(item):
        index_list, labels = get_clusters(6, item)

        lst = []
        for i in index_list:
            lst2 = []
            for j in i:
                try:
                    lst2.append(coord_list[j])
                except:
                    pass
            lst.append(lst2)
        return lst

    doublelst = []
    x = 0
    for i in coords:
        coord_list = total[x]
        doublelst.append(transfer_to_coords(i))
        x+=1
    return doublelst


def cluster_main(data):
    xlst, ylst= split_xy(data)
       #Kmeans toepassen:
    #Voorbeeld scatterplot:
    plt.scatter(xlst,ylst,marker='o')
    plt.gcf().set_size_inches((10, 10))
    plt.show()
    index_list, labels = get_clusters(8,data)
    plt.scatter(xlst, ylst, c=labels)
    plt.show()
    total_list = get_coords(index_list,data)
    return get_coords(index_list,data),total_list
