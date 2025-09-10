import numpy as np

options = [[1, 2, -3, 2, 0, -1, 2, -1, 0],
           [-1],
           [0, -1, 1, 0, 3],
           [0, 1],
           [-0.0635, 0, 0.3007, 0.5000, 0.3007, 0, -0.0635],
           [0.0143, 0.0490, 0.1179, 0.1997, 0.2381, 0.1997, 0.1179, 0.0490, 0.0143]]


def blackbox(xx, option):
    if 0 < option <= 6:
        return np.convolve(xx, options[option - 1])
    else:
        raise ValueError
