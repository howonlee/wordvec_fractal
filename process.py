import numpy as np
import matplotlib.pyplot as plt

def sierpinski(order=5):
    # for testing
    gen = np.array([[1,1],[1,0]])
    arr = np.copy(gen)
    for x in xrange(order-1):
        arr = np.kron(arr, gen)
    return arr

def mat_to_points(mat):
    points = []
    for x in xrange(mat.shape[0]):
        for y in xrange(mat.shape[1]):
            if mat[x,y] > 0:
                points.append(
                        (
                            (float(x) / mat.shape[0]),
                            (float(y) / mat.shape[1])
                        )
                )
    return points

def box_hash(point, div):
    point = list(point)
    point = map(lambda x: int(x * prod) // div, point)
    return tuple(point)

def num_boxes(points, div):
    boxes = set()
    for point in points:
        hsh = box_hash(point, div)
        boxes.add(hsh)
    return len(boxes)

if __name__ == "__main__":
    test_pts = mat_to_points(sierpinski(order=9))
    boxes = []
    for x in [8,16,32,64,128,256,512,1024]:
        boxes.append(num_boxes(test_pts, x))
    plt.plot(boxes)
    plt.show()
