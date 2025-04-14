import math
h, tau = 0.1, 0.05
gamma = tau**2/h**2
psi = []
l_matrix = []
t_matrix = []
for _ in range (0, 11):
    l_matrix.append(_/10)
for _ in range (0, 11):
    t_matrix.append(_/20)
for _ in range (1, 10):
    psi.append(math.sin(l_matrix[_]+0.2))

U=[[0 for i in range(11)] for j in range(11)]
for _ in range (0, 11):
    U[_][0] = t_matrix[_]-0.5
    U[_][-1] = 3 * t_matrix[_]

for _ in range (1, 10):
    U[0][_] = (l_matrix[_]+0.5)*(l_matrix[_]-1)

for j in range(1, 10):
    U[1][j] = U[0][j] + tau * psi[j-1] + (tau**2/2) * (U[0][j+1] - 2*U[0][j]+U[0][j-1]) / h**2

for i in range (2, 11):
    for j in range(1, 10):
        U[i][j] = 2 * U[i-1][j] - U[i-2][j] + gamma * (U[i-1][j+1] - 2*U[i-1][j]+U[i-1][j-1])
for row in U:
    print(" ".join(f"{val:.3f}" for val in row))