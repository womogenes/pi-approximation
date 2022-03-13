import os

if os.path.basename(os.getcwd()) == "algorithms":
    PI_PATH = os.path.abspath("../pi.txt")
else:
    PI_PATH = os.path.abspath("./pi.txt")

with open(PI_PATH) as fin:
    pi_str = fin.read()


def evaluate(pi_approx):
    i = 0
    approx_str = str(pi_approx)

    while i < len(pi_str) and approx_str[i] == pi_str[i]:
        i += 1

    return i - 1
