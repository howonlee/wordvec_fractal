import numpy as np

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

def box_hash(point, mod, prod=10000):
    point = list(point)
    point = map(lambda x: int(x * prod), point)
    return point

if __name__ == "__main__":
    test_pts = mat_to_points(sierpinski(order=3))
    for point in test_pts:
        print box_hash(point, 5)
