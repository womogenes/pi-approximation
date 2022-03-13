from mpmath import mp, mpf
import sys
import random


def circle(iters=pow(10, 6)):
    # Find if a random point falls inside the unit circle
    inside = 0

    for _ in range(iters):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1

    return inside / iters * 4


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 20

    pi = circle()
    print(pi)
    print(evaluate(pi))
