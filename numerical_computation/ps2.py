import numpy as np
import matplotlib.pyplot as plt
import time
from copy import deepcopy

start_time = time.time()

def get_A(n, _type):
    A = np.zeros((n+1, n+1))
    for i in range(n+1):
        x = 1 + 0.2*i
        for j in range(n+1):
            A[i][j] = (1+0.2*i)**j if _type==1 else 1/(i+j+1)
    b = np.sum(A, axis=1, keepdims=True)
    return A, b

#q1
print("="*35, "q1", "="*35)
for n in range(4, 9):
    A1, _ = get_A(n, 1)
    A2, _ = get_A(n, 2)
    print(f"n={n}, A1条件数:{np.linalg.cond(A1,2)}, A2条件数:{np.linalg.cond(A2,2)}")

#q2
print("="*35, "q2", "="*35)
A1, b1 = get_A(5, 1)
A2, b2 = get_A(5, 2)
A1_ori = deepcopy(A1)
A2_ori = deepcopy(A2)
x1 = np.linalg.solve(A1, b1)
x2 = np.linalg.solve(A2, b2)
print(f"x1:\n{x1},\nx2:\n{x2}")

#q3
print("="*35, "q3", "="*35)
A1[1][1] += 1e-12
A1[5][5] += 1e-12
A1_delta = A1 - A1_ori
x1_tilde = np.linalg.solve(A1, b1)
print(f"x1_tilde:\n{x1_tilde}")

#q4
print("="*35, "q4", "="*35)
A2[1][1] += 1e-7
A2[5][5] += 1e-7
A2_delta = A2 - A2_ori
x2_tilde = np.linalg.solve(A2, b2)
A2, b2 = get_A(5, 2)
b2_ori = deepcopy(b2)
b2[5][0] += 1e-4
b2_delta = b2 - b2_ori
x2_overline = np.linalg.solve(A2, b2)
print(f"x2_tilde:\n{x2_tilde},\nx2_overline:\n{x2_overline}")

#q6
print("="*35, "q6", "="*35)
delta1 = np.linalg.norm(x1-x1_tilde, ord=np.inf)/np.linalg.norm(x1, ord=np.inf)
delta2 = np.linalg.norm(x2-x2_tilde, ord=np.inf)/np.linalg.norm(x2, ord=np.inf)
delta3 = np.linalg.norm(x2-x2_overline, ord=np.inf)/np.linalg.norm(x2, ord=np.inf)
g = lambda x: x/(1-x)
_delta1 = g(np.linalg.cond(A1_ori, np.inf)*np.linalg.norm(A1_delta, ord=np.inf)/np.linalg.norm(A1_ori, ord=np.inf))
_delta2 = g(np.linalg.cond(A2_ori, np.inf)*np.linalg.norm(A2_delta, ord=np.inf)/np.linalg.norm(A2_ori, ord=np.inf))
_delta3 = np.linalg.cond(A2_ori, np.inf)*np.linalg.norm(b2_delta, ord=np.inf)/np.linalg.norm(b2_ori, ord=np.inf)
print(f"delta1: {delta1}, 理论值: {_delta1}")
print(f"delta2: {delta2}, 理论值: {_delta2}")
print(f"delta3: {delta3}, 理论值: {_delta3}")

end_time = time.time()
print(f"CPU Time Cost: {end_time-start_time} s")