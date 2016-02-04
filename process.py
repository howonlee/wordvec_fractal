import numpy as np

def sierpinski(order=5):
    # for testing
    gen = np.array([[1,1],[1,0]])
    arr = np.copy(gen)
    for x in xrange(order-1):
        arr = np.kron(arr, gen)
    return arr

def box_hash(point, mod, prod=10000):
    point = list(point)
    point = map(lambda x: int(x * prod), point)
    return point

if __name__ == "__main__":
    print sierpinski(order=3)
    # print box_hash(np.array([0.2, 0.3]), 5)
