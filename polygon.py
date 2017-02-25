'''
n-gon metric...
for...reasons
'''
import math
def arg(x, y): 
    if x == 0 and y == 0:
        return 0
    return math.acos(x / math.hypot(x, y))
    
class Polygon:
    '''a regular convex polygon'''
    
    def __init__(self, sides=3, angle=0, center = (0,0), radius = 200):
        self.sides = sides
        self.angle = angle
        self.center = center
        self.radius = radius
        self.interior_angle = math.pi * (sides-2)/(sides)
        self.sidelabels = list()
        for i in range(self.sides): self.sidelabels.append(i)
        self.exterior_angle = math.pi - self.interior_angle
        self.vertices = []
        for i in range(self.sides):
            self.vertices.append(
            (self.radius*math.cos(self.angle + i * (2 * math.pi / self.sides)),
            self.radius*math.sin(self.angle + i * (2 * math.pi / self.sides))))
        
    
    def getSideangle(self, side):
        '''side i's angle to the x-axis
        '''
        side = side % self.sides
        if side < (self.sides - 1):
            return arg(self.vertices[side+1][0] - self.vertices[side][0],
            self.vertices[side+1][1] - self.vertices[side][1])
        else:
            return arg(self.vertices[0][0] - self.vertices[side][0],
            self.vertices[0][1] - self.vertices[side][1])
        
    def polygonal_norm(x,y):
        '''returns polygonal norm for the point x,y relative to Polygon
        this is the distance from the center to the nearest point, Z, on the 
        polygon where the polygon is the unique n-gon centered at center 
        containing M = (x, y) '''
        arg_M = arg(x, y)
        #find which face the pont is closest to
        def triangle(x,y):
            for i in self.sidelabels:
                if self.angle + 2*math.pi / self.sides * i <= arg_M \
                < self.angle + 2*math.pi / self.sides * (i+1):
                    return i
        return 'TODO'