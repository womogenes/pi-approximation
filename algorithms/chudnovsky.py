from decimal import Decimal, getcontext
import sys


def chudnovsky(iters=pow(10, 5)):
    summation = 0
    for i in range(iters):
        num = mp.fac(6 * i) * (545140134 * i + 13591409)
        denom = mp.fac(3 * i) * mp.power(mp.fac(i), 3) * \
            mp.power(-262537412640768000, i)
        summation += num / denom

    c = 426880 * mp.sqrt(10005)

    return c / summation


if __name__ == "__main__":
    getcontext().prec = pow(10, 5)
    pi = chudnovsky()

    print(pi)
