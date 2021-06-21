import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


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


def get_clusters(cluster_aantal, lst):
    model_kmeans = KMeans(n_clusters=cluster_aantal).fit(lst)
    labels = list(model_kmeans.labels_)
    new = []
    for i in range(cluster_aantal):
        new.append(get_indexi(labels, i))
    return new, labels

def get_coords(data,lst):
    total = []
    for i in lst:
        new = []
        for j in i:
            new.append(data[j])
        total.append(new)
    return total

def sort_coords(coords):
    for i in coords:
        index_list, labels = get_clusters(5,i)
        plt.scatter(i[:, 0], i[:, 1], c=labels)
    return None

def array_to_list(lst):
    '''
    Turns list of arrays into list of lists
    :param lst: Input list of np.arrays
    :return: List of lists
    '''
    returnable = []
    for i in lst:
        new = []
        for j in i:
            new.append(list(j))
        returnable.append(new)
    return returnable

#Kmeans toepassen:
#Voorbeeld scatterplot:
def cluster_data(data):
    lstx = []
    lsty = []
    for i in data:
        lstx.append(i[0])
        lsty.append(i[1])
    print(lstx)
    print(data)
    index_list, labels = get_clusters(5, data)
    print(labels)
    plt.scatter(lstx, lsty, c=labels)
    coords = array_to_list(get_coords(data, index_list))
    for i in coords:
        index_list, labels = get_clusters(5, i)
