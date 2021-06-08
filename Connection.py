from math import sqrt
class Connection():
    def __init__(self,town_a,town_b):
        self.start = town_a
        self.end = town_b
    def get_towns(self):
        return self.start, self.end
    def get_distance(self):
        return sqrt((self.start[0] - self.end[0])**2 + (self.start[1] - self.end[1])**2)


