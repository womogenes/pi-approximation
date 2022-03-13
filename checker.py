from evaluate import *
import os
from tabulate import tabulate
from mpmath import mp
import sys
sys.path.append("algorithms")

mp.dps = 128


# Terrible way to import things
algos = os.listdir("./algorithms")
for algo in algos:
    if algo == "__pycache__":
        continue
    exec(f"from {algo[:-3]} import *")

# Read from file
with open("./pi.txt") as fin:
    pi_str = fin.read()

# Define approximation methods
methods = {
    "Gauss-Legendre": gauss_legendre,
    "Gaussian integral": gaussian_integral,
    "Chudnovsky": chudnovsky,
    "Leibniz": leibniz
}

values = [[name, evaluate(str(methods[name]()))] for name in methods]

print(tabulate(values, headers=["Method", "Value"],
      tablefmt="github", disable_numparse=True))
