from mpmath import mp, mpf
import sys


def basel(iters=pow(10, 6)):
    s = 0
    for i in range(1, iters + 1):
        s += 1 / (mpf(i) ** 2)

    return mp.sqrt(s * 6)


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 100

    pi = basel()

    print(pi)
    print(evaluate(pi))
