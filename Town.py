'''
This file was deprecated on June the 18th
The Class has been reworked on June the 28th
'''


class Town:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.visited = False

    def get_coords(self):
        return [self.x,self.y]
