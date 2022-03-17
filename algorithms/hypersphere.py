# https://en.wikipedia.org/wiki/Volume_of_an_n-ball
from mpmath import mp, mpf
import sys
import random


def hypersphere(iters=pow(10, 6)):
    # Find if a random point falls inside the unit hypersphere
    inside = 0

    for _ in range(iters):
        x, y, z, w = [random.uniform(-1, 1) for _ in range(4)]
        if x**2 + y**2 + z**2 + w**2 <= 1:
            inside += 1

    return mp.sqrt(inside / iters * 32)


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 20

    pi = hypersphere()
    print(pi)
    print(evaluate(pi))
