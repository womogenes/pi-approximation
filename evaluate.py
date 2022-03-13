with open("./pi.txt") as fin:
    pi_str = fin.read()

def evaluate(pi_approx):
    i = 0

    while i < len(pi_approx) and pi_approx[i] == pi_str[i]:
        i += 1
    return pi_approx[:i]