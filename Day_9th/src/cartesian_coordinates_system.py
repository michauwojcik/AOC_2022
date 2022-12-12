import numpy as np

class CartesianCoordinateSystem:
    
    UNIT_VECTORS = {
        "L": np.array((-1,  0)),
        "U": np.array(( 0,  1)),
        "R": np.array(( 1,  0)),
        "D": np.array(( 0, -1))
    }
    
    ORIGIN = np.array([0, 0])
    
    def __init__(self):
        ...
        
    
    def create_vector(self, direction: str, value: float):
        return value * self.UNIT_VECTORS[direction]


    def get_unit_vector(self, direction: str):
        return self.UNIT_VECTORS[direction]


    def check_point_neighborhood(self, p1: np.array, p2: np.array, radius=1):
        """
        Checks whether p2 is in p1's neighborhood
        """

        if (abs(p2[0] - p1[0]) <= radius) & (abs(p2[1] - p1[1]) <= radius):
            return True

        return False