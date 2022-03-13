from mpmath import mp

def gaussian_integral():
    return mp.quad(lambda x: mp.exp(-x ** 2), [-mp.inf, mp.inf]) ** 2