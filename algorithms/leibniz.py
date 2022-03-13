import sys
from decimal import Decimal, getcontext


def leibniz(iters=pow(10, 6)):
    s = 0
    for i in range(iters):
        s += Decimal(-1) ** i / (2 * i + 1)

    return s * 4


if __name__ == "__main__":
    getcontext().prec = 10
    sys.path.append("..")
    from evaluate import evaluate

    pi = leibniz()
    print(pi)
    print(evaluate(pi))
