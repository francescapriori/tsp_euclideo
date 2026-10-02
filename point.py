import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, pj):
        return math.sqrt((self.x - pj.x) ** 2 + (self.y - pj.y) ** 2)