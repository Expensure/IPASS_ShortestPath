import random  # moet gebruikt worden, kan nooit op een andere manier starten
import numpy as np  # moet gebruikt worden voor argsort


# Eigen vorm van kmeans, maar ik ben er zo ontevreden mee dat ik hem niet ga gebruiken.
def sum_scuffed(lst):
    total = 0
    for i in lst:
        total += i
    return total


class KMeans:
    def __init__(self, distance_matrix, n_clusters=2, start_prob=0.90, end_prob=0.99):
        if not 0 <= start_prob < end_prob <= 1:
            raise ValueError('start_prob must be smaller than end_prob.')
        if not n_clusters < len(distance_matrix):
            raise ValueError('number of clusters must not exceed number of data points.')

        self.distance_matrix = distance_matrix
        self.n_clusters = n_clusters
        self.n_points = len(distance_matrix)
        self.start_prob = start_prob
        self.end_prob = end_prob
        self.clusters = None
        self.kmeans = None

    def init_kmeans(self):
        means = [random.randint(0, self.n_points - 1)]
        while len(means) != self.n_clusters:
            distances = [self.closest_means(means, point)[1] for point in range(self.n_points)]
            distances_index = np.argsort(distances)
            start_index = int(self.start_prob * len(distances_index))
            end_index = round(self.end_prob * (len(distances_index) - 1))
            new_mean = distances_index[random.randint(start_index, end_index)]
            means.append(new_mean)
        return means

    def get_distance(self, point1, point2):
        return self.distance_matrix[point1][point2]

    def closest_means(self, means, point):
        #Vindt dichtsbijzijnde item bij aangegeven punt
        closest_mean = None
        closest_distance = float('inf')

        for mean in means:
            distance = self.get_distance(point, mean)
            if distance < closest_distance:
                closest_mean = mean
                closest_distance = distance

        return closest_mean, closest_distance

    def associate_points_to_closest_medoid(self, means):
        clusters = {mean: [mean] for mean in means}
        for point in range(self.n_points):
            mean, _ = self.closest_means(means, point)
            clusters[mean].append(point)
        return clusters

    def get_mean_cost(self, means, clusters):
        return sum_scuffed([self.get_distance(point, means) for point in clusters[means]]) / \
               len(([self.get_distance(point, means) for point in clusters[means]]))

    def get_configuration_cost(self, means, clusters):
        return sum_scuffed([self.get_mean_cost(means, clusters) for means in means])

    def get_non_means(self, means, clusters):
        return [pt for points in clusters.values() for pt in points if pt not in means]

    # https://en.wikipedia.org/wiki/K-medoids
    def run(self, max_iterations=10, tolerance=0.01):
        # 1- Initialize: select k of the n data points as the medoids.
        self.kmeans = self.init_kmeans()

        # 2- Associate each data point to the closest medoid.
        self.clusters = self.associate_points_to_closest_medoid(self.kmeans)

        # 3- While the cost of the configuration decreases:
        # 3.1- For each means m, for each non-means data point o:
        # 3.1.1- Swap m and o, associate each data point to the closest means, recompute the cost (sum of distances of points to their medoid)
        # 3.1.2- If the total cost of the configuration increased in the previous step, undo the swap
        cost_change = float('inf')
        current_cost = self.get_configuration_cost(self.kmeans, self.clusters)
        for _ in range(max_iterations):
            if cost_change > tolerance:
                cost_change = 0
                for m in self.kmeans:
                    for o in self.get_non_means(self.kmeans, self.clusters):
                        new_means = [o] + [med for med in self.kmeans if med != m]
                        new_clusters = self.associate_points_to_closest_medoid(new_means)
                        new_cost = self.get_configuration_cost(new_means, new_clusters)
                        if new_cost < current_cost:
                            self.kmeans = new_means
                            self.clusters = new_clusters
                            cost_change = current_cost - new_cost
                            current_cost = new_cost
                            break
            else:
                break


