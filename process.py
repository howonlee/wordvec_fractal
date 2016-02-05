import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import datetime
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
    circle = ((xx - 100) ** 2 + (yy - 100) ** 2) < 6400
    plt.imshow(circle)
    plt.show()
    return circle

def mat_to_points(mat):
    points = []
    for x in xrange(mat.shape[0]):
        for y in xrange(mat.shape[1]):
            if mat[x,y] > 0:
                points.append(np.array((float(x) / mat.shape[0], float(y) / mat.shape[1])))
    print "num points: ", len(points)
    return points

def sqrt_dist(fst, snd):
    # normal folks dist
    return np.sqrt(np.sum((fst - snd) ** 2))

def memoize_distances(pts, dist_fn=sqrt_dist):
    distances = []
    ctr = 0
    total = len(pts) ** 2
    for pt1, pt2 in itertools.product(pts, pts):
        ctr += 1
        if ctr % 500000 == 0:
            print "memoizing: ", ctr, " / ", total, " : ", datetime.datetime.now()
        distances.append(dist_fn(pt1, pt2))
    return distances

def correlation_integral(distances, epsilon):
    return float(len([1 for dist in distances if dist < epsilon])) / float(len(distances))

def sierpinski_correlation():
    # circle is a c&p of this, only it takes an obnoxiously long time
    sierpinski_points = mat_to_points(sierpinski())
    epsilons = np.logspace(-5, -2, num=10, base=2.0)
    print epsilons
    div_epsilons = np.array([np.log2(epsilon / epsilons[0]) for epsilon in epsilons])
    log_correlation_integrals = []
    distances = memoize_distances(sierpinski_points)
    for epsilon in epsilons:
        print epsilon, " : starting..."
        log_correlation_integrals.append(np.log2(correlation_integral(distances, epsilon)))
        print "done"
    p = np.polyfit(div_epsilons, log_correlation_integrals, 1)
    plt.plot(div_epsilons, log_correlation_integrals, "k.", label="correlation integrals")
    plt.plot(div_epsilons, np.polyval(p, div_epsilons), 'r-', label="least squares fit")
    plt.legend(loc=1) # upper left
    plt.title("Correlation dimension for Sierpinski Triangle: slope = " + str(p[0]))
    plt.xlabel("log(epsilons / epsilons(0)), epsilons(0) chosen arbitrarily")
    plt.ylabel("log(correlation integrals)")
    plt.savefig("sierpinski")

def word2vec_correlation(filename="vecs.txt"):
    with open(filename) as word2vec_file:
        vecs = word2vec_file.readlines()[1:]
        vec_points = []
        for vec in vecs:
            np_vec = np.array(map(float, vec.split()[1:]))
            vec_points.append(np_vec)
        vec_points = random.sample(vec_points, 10000)
    epsilons = np.logspace(-1.5, -0.5, num=30, base=2.0)
    print epsilons
    div_epsilons = np.array([np.log2(epsilon / epsilons[0]) for epsilon in epsilons])
    log_correlation_integrals = []
    distances = memoize_distances(vec_points)
    for epsilon in epsilons:
        print epsilon, " : starting..."
        log_correlation_integrals.append(np.log2(correlation_integral(distances, epsilon)))
        print "done"
    p = np.polyfit(div_epsilons, log_correlation_integrals, 1)
    plt.plot(div_epsilons, log_correlation_integrals, "k.", label="correlation integrals")
    plt.plot(div_epsilons, np.polyval(p, div_epsilons), 'r-', label="least squares fit")
    plt.legend(loc=0) # upper left
    plt.title("Correlation dimension for Word2Vec Points: slope = " + str(p[0])[:5])
    plt.xlabel("log(epsilons / epsilons(0)), epsilons(0) chosen arbitrarily")
    plt.ylabel("log(correlation integrals)")
    plt.savefig("word2vec")

if __name__ == "__main__":
    matplotlib.rcParams['figure.figsize'] = (8,5)
    matplotlib.rcParams['savefig.dpi'] = 100
    word2vec_correlation()
