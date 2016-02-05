import numpy as np
import matplotlib.pyplot as plt
import itertools

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
                points.append(np.array((float(x) / mat.shape[0], float(y) / mat.shape[1])))
    return points

def l2_dist(fst, snd):
    return np.sum((fst - snd) ** 2)

def correlation_integral(points, epsilon, dist_fn=l2_dist):
    num_corrs = 0
    for point1, point2 in itertools.product(points, points):
        if dist_fn(point1, point2) < epsilon:
            num_corrs += 1
    return float(num_corrs) / float(len(points) ** 2)

if __name__ == "__main__":
    sierpinski_points = mat_to_points(sierpinski(5))
    epsilons = [0.0005, 0.001, 0.002, 0.004, 0.008, 0.016, 0.032, 0.064]
    correlation_integrals = []
    for epsilon in epsilons:
        correlation_integrals.append(correlation_integral(sierpinski_points, epsilon))
    plt.loglog(epsilons, correlation_integrals, "o")
    plt.title("Correlation dimension for sierpinski") ########### !!!
    plt.xlabel("epsilons")
    plt.xlabel("correlation integrals")
    plt.show()
