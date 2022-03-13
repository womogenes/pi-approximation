from mpmath import mp
import sys


def circle_integral():
    return mp.quad(lambda x: mp.sqrt(1 - x**2), [0, 1]) * 4


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 1000

    pi = circle_integral()
    print(pi)
    print(evaluate(pi))
