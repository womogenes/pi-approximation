from mpmath import mp, mpf, power
import sys


def arctan(x, terms=pow(10, 5)):
    # Taylor series (https://en.wikipedia.org/wiki/Machin-like_formula)
    s = mpf(0)

    for n in range(terms):
        s += mpf(-1)**n / (2*n + 1) * power(x, 2*n + 1)

    return s


def machin(iters=pow(10, 5)):
    yield arctan(1) * 4
    yield (arctan(mpf(1/2)) + arctan(mpf(1/3))) * 4
    yield (4 * arctan(mpf(1/5)) - arctan(mpf(1/239))) * 4


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 20

    for pi in machin():
        print(pi, evaluate(pi))
