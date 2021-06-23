'''
Deprecated since 16th of June
'''

import numpy as np

class Score:
    '''
    Berekent afstand van een pad, om gebruikt te worden in Machine learning
    '''

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
        fitness = 0
        # Berekent lengte van het pad tussen elk punt
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


