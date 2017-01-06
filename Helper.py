import numpy as np


class XYZ:
    X, Y, Z = 0, 0, 0

    def __init__(self, value):
        value_type = type(value).__name__

        if value_type == 'dict':
            self.X, self.Y, self.Z = value['x'], value['y'], value['z']
        elif value_type == 'list' or value_type == 'ndarray':
            self.X, self.Y, self.Z = value[0], value[1], value[2]
        else:
            self.X, self.Y, self.Z = value.X, value.Y, value.Z

    def to_array(self):
        return np.array([self.X, self.Y, self.Z], dtype=float)

    def to_object(self):
        return self

    def to_dict(self):
        return {'x': self.X, 'y': self.Y, 'z': self.Z}

    def is_null(self):
        return np.all(self.to_array() == 0)

    def not_null(self):
        return not self.is_null()


def get_distance(a, b):
    a = XYZ(a).to_array()
    b = XYZ(b).to_array()

    return np.linalg.norm(a - b)
