from mpmath import mp
import sys


def gaussian_integral():
    return mp.quad(lambda x: mp.exp(-x ** 2), [-mp.inf, mp.inf]) ** 2


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 150

    pi = gaussian_integral()
    print(pi)
    print(evaluate(pi))
