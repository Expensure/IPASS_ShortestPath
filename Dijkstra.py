import numpy as np


class Dijkstra:
    """
        >>> import mlrose
        >>> import numpy as np
        >>> coords = [(0, 0), (3, 0), (3, 2), (2, 4), (1, 3)]
        >>> dists = [(0, 1, 3), (0, 2, 5), (0, 3, 1), (0, 4, 7), (1, 3, 6),
                     (4, 1, 9), (2, 3, 8), (2, 4, 2), (3, 2, 8), (3, 4, 4)]
        >>> fitness_coords = mlrose.TravellingSales(coords=coords)
        >>> state = np.array([0, 1, 4, 3, 2])
        >>> fitness_coords.evaluate(state)
        13.86138...
        >>> fitness_dists = mlrose.TravellingSales(distances=dists)
        >>> fitness_dists.evaluate(state)

    """

    def __init__(self, coords, distances):
        if coords is None and distances is None:
            raise Exception("At least one of coords and distances must be" + " specified.")
        if coords is not None:
            self.is_coords = True
            path_list = []
            dist_list = []
        else:
            self.is_coords = False
            # Split into separate lists to save data
            node1_list, node2_list, dist_list = zip(*distances)

            if min(dist_list) <= 0:
                raise Exception("The distance between each pair of nodes"+ " must be greater than 0.")
            if min(node1_list + node2_list) < 0:
                raise Exception("The minimum node value must be 0.")

            if not max(node1_list + node2_list) == \
                   (len(set(node1_list + node2_list)) - 1):
                raise Exception("All nodes must appear at least once in"
                                + " distances.")

            path_list = list(zip(node1_list, node2_list))

        self.coords = coords
        self.distances = distances
        self.path_list = path_list
        self.dist_list = dist_list

    def evaluate(self, state):
        """Evaluate the fitness of a state vector.
        Parameters
        ----------
        state: array
            State array for evaluation. Each integer between 0 and
            (len(state) - 1), inclusive must appear exactly once in the array.
        Returns
        -------
        fitness: float
            Value of fitness function. Returns :code:`np.inf` if travel between
            two consecutive nodes on the tour is not possible.
        """

        fitness = 0

        # Calculate length of each leg of journey
        for i in range(len(state) - 1):
            node1 = state[i]
            node2 = state[i + 1]

            if self.is_coords:
                fitness += np.linalg.norm(np.array(self.coords[node1]) - np.array(self.coords[node2]))
            else:
                path = (min(node1, node2), max(node1, node2))

                if path in self.path_list:
                    fitness += self.dist_list[self.path_list.index(path)]
                else:
                    fitness += np.inf

        # Calculate length of final leg
        node1 = state[-1]
        node2 = state[0]

        if self.is_coords:
            fitness += np.linalg.norm(np.array(self.coords[node1])
                                      - np.array(self.coords[node2]))
        else:
            path = (min(node1, node2), max(node1, node2))

            if path in self.path_list:
                fitness += self.dist_list[self.path_list.index(path)]
            else:
                fitness += np.inf

        return fitness
