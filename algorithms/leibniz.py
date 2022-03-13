from mpmath import mp, mpf

def leibniz(iters=1<<16):
    s = 0
    for i in range(iters):
        s += mpf(-1) ** i / (2 * i + 1)

    return s * 4

if __name__ == "__main__":
    pi = leibniz()
    print(pi)