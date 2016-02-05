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
    xx, yy = np.mgrid[:80, :80]
    circle = ((xx - 40) ** 2 + (yy - 40) ** 2) < 150
    plt.imshow(circle)
    plt.show()
    return circle

def mat_to_points(mat):
    points = []
    for x in xrange(mat.shape[0]):
        for y in xrange(mat.shape[1]):
            if mat[x,y] > 0:
                points.append(np.array((float(x) / mat.shape[0], float(y) / mat.shape[1])))
    return points

def sqrt_dist(fst, snd):
    # normal folks dist
    return np.sqrt(np.sum((fst - snd) ** 2))

def correlation_integral(points, epsilon, dist_fn=sqrt_dist):
    num_corrs = 0
    for point1, point2 in itertools.product(points, points):
        if dist_fn(point1, point2) < epsilon:
            num_corrs += 1
    return float(num_corrs) / float(len(points) ** 2)

if __name__ == "__main__":
    sierpinski_points = mat_to_points(sierpinski())
    epsilons = np.logspace(-4, -1, num=10, base=2.0)
    print epsilons
    div_epsilons = np.array([np.log2(epsilon / epsilons[0]) for epsilon in epsilons])
    log_correlation_integrals = []
    for epsilon in epsilons:
        print epsilon, " : starting..."
        log_correlation_integrals.append(np.log2(correlation_integral(sierpinski_points, epsilon)))
        print "done"
    p = np.polyfit(div_epsilons, log_correlation_integrals, 1)
    print p
    plt.plot(div_epsilons, log_correlation_integrals, "k.")
    plt.plot(div_epsilons, np.polyval(p, div_epsilons), 'r-')
    plt.title("Correlation dimension for sierpinski") ########### !!!
    plt.xlabel("log(epsilons / epsilons(0)), epsilons(0) chosen arbitrarily")
    plt.ylabel("log(correlation integrals)")
    plt.show()
