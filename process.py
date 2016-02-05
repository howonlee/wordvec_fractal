import numpy as np
import matplotlib.pyplot as plt

def sierpinski(order=5):
    # for testing
    gen = np.array([[1,1],[1,0]])
    arr = np.copy(gen)
    for x in xrange(order-1):
        arr = np.kron(arr, gen)
    return arr

def circle():
    xx, yy = np.mgrid[:200, :200]
    circle = (xx - 100) ** 2 + (yy - 100) ** 2
    donut = np.logical_and(circle < (6400 + 60), circle > (6400 - 60))
    print donut
    return donut

def mat_to_points(mat):
    points = []
    for x in xrange(mat.shape[0]):
        for y in xrange(mat.shape[1]):
            if mat[x,y] > 0:
                points.append((float(x), float(y)))
    return points

### correlation dimension time, friends

if __name__ == "__main__":
