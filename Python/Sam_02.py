# Define a class Point having x and y coordinates as data members. Add appropriate
# constructor, destructor. Add a method that computes and returns the distance between
# 2 points.
# d=√((x2 – x1)² + (y2 – y1)²)

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point created!")
    
    def __del__(self):
        print("Point destroyed!")
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)
        

p1 = Point(3, 3)
p2 = Point(3, 0)
print("The distance is:",p1.distance(p2),"units")
del p1
del p2
