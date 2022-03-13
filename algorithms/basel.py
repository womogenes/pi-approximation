from mpmath import mp, mpf


def basel(iters=pow(10, 5)):
    s = 0
    for i in range(1, iters + 1):
        s += 1 / (mpf(i) ** 2)

    return mp.sqrt(s * 6)


if __name__ == "__main__":
    pi = basel()
    print(pi)
