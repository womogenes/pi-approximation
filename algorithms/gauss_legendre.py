from mpmath import mp, mpf
import sys


def get_pi(a, b, t):
    return (a + b) ** 2 / (4 * t)


def gauss_legendre(iters=16):
    a = 1
    b = 1 / mpf(mp.sqrt(2))
    t = mpf("1/4")
    p = 1

    for _ in range(iters):
        a_next = (a + b) / 2
        b_next = mp.sqrt(a * b)
        t_next = t - p * (a - a_next) ** 2
        p_next = p << 1

        a, b, t, p = a_next, b_next, t_next, p_next

        cur = get_pi(a, b, t)

    return get_pi(a, b, t)


if __name__ == "__main__":
    sys.path.append("..")
    from evaluate import evaluate
    mp.dps = 1000000

    pi = gauss_legendre()
    print(str(pi)[:100] + "...")
    print(evaluate(pi))
