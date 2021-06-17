import numpy as np

class Score:
    """Fitness function for Travelling Salesman optimization problem.
    coords: list of pairs, default: None
        list of the (x, y) coordinates of all nodes (where i
        gives the coordinates of node i). This assumes that travel between
        all pairs of nodes is possible.
    distances: list of triples, default: None
        List giving the distances, d, between all pairs of nodes, u and v, for
        which travel is possible, with each list item in the form (u, v, d).
        Order of the nodes does not matter, so (u, v, d) and (v, u, d) are
        considered to be the same. If a pair is missing from the list, it is
        assumed that travel between the two nodes is not possible. This
        argument is ignored if coords is not :code:`None`.

    Note
    ----
    1. The TravellingSales fitness function is suitable for use in travelling
       salesperson (tsp) optimization problems *only*.
    2. It is necessary to specify at least one of :code:`coords` and
       :code:`distances` in initializing a TravellingSales fitness function
       object.
    """

    def __init__(self, coords=None):

        if coords is None:
            raise Exception("""At least one of coords and distances must be"""
                            + """ specified.""")
        else:
            self.is_coords = True
            path_list = []
            dist_list = []

        self.coords = coords
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
        followed_path = []
        for i in range(len(state) - 1):
            node1 = state[i]
            followed_path.append(node1)
            node2 = state[i + 1]

            if self.is_coords:
                fitness += np.linalg.norm(np.array(self.coords[node1])
                                          - np.array(self.coords[node2]))
            else:
                path = (min(node1, node2), max(node1, node2))

                if path in self.path_list:
                    fitness += self.dist_list[self.path_list.index(path)]
                else:
                    fitness += np.inf

        # Calculate length of final leg
        node1 = state[-1]
        node2 = state[0]
        followed_path.append(node1)
        if self.is_coords:
            fitness += np.linalg.norm(np.array(self.coords[node1])
                                      - np.array(self.coords[node2]))
        else:
            path = (min(node1, node2), max(node1, node2))

            if path in self.path_list:
                fitness += self.dist_list[self.path_list.index(path)]
            else:
                fitness += np.inf
        return fitness, followed_path


