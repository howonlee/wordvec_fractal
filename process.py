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

def box_hash(point, box_size):
    point = list(point)
    point = map(lambda x: (x) // box_size, point)
    return tuple(point)

def num_boxes(points, box_size):
    boxes = set()
    for point in points:
        hsh = box_hash(point, box_size)
        boxes.add(hsh)
    return len(boxes)

if __name__ == "__main__":
    # test_pts = mat_to_points(sierpinski(order=9))
    test_pts = mat_to_points(circle())
    print test_pts
    boxes = []
    for x in [1,2,4,8,16,32,64]:
        boxes.append(num_boxes(test_pts, x))
    plt.loglog(boxes)
    plt.show()
