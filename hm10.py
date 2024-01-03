import numpy as np

def solve_polynomial(NUM1):
    roots = np.roots(NUM2)
    return roots

NUM1 = [1, 0, 0, 0, 0, 1]
NUM2 = [1, 0, 3, 0, 0, 0, 0, 0, 1]

p1 = solve_polynomial(NUM1)
p2 = solve_polynomial(NUM2)

print("P1:", p1)
print("P2:", p2)
