from mpmath import mp, mpf
import sys


def leibniz(iters=pow(10, 5)):
    s = 0
    for i in range(iters):
        s += mpf(-1) ** i / (2 * i + 1)

    return s * 4


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 20

    pi = leibniz()
    print(pi)
    print(evaluate(pi))
