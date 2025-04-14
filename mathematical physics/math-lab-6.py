import math
k, s, l, h, m, p, lamda, c, T1, T2, tau = 4, 1, 0.5, 0.1, 3, 11350, 35.1, 0.127, 4, 160, 1/6
a1 = 1/4
a2 = lamda / (c * p)
l_matrix = []
K = []
kl_matrix = []
a = []
b = []
c = []
alpha=[[0 for i in range(5)] for j in range(3)]
beta=[[0 for i in range(5)] for j in range(3)]
for i in range (0, 5):
    kl_matrix.append(i/10+0.05)
    K.append(a2*math.exp(-a1*kl_matrix[i]))
for i in range(0, 6):
    l_matrix.append(i/10)
U=[[0 for i in range(6)] for j in range(4)]

for i in range(0, 4):
    U[i][0] = T1
    U[i][5] = T2
for j in range(1, 5):
    U[0][j] = ((T2 - T1) / l ** 2 * l_matrix[j] ** 2 + T1)
#print(l_matrix) debug

for _ in range(4):
    a.append((tau / h ** 2) * K[_])
    b.append((tau / h ** 2) * K[_+1])
    c.append(a[_] + b[_] + 1)

for j in range(0,3):
    alpha[j][0] = 0
    beta[j][0] = 4
    for i in range(1, 5):
        alpha[j][i] = b[i-1] / (c[i-1] - a[i-1] * alpha[j][i-1])
        beta[j][i] = (a[i-1] * beta[j][i-1] + U[j][i]) / (c[i-1] - a[i-1] * alpha[j][i-1])
        #print (a[i-1], beta[j][i-1], U[j][i]) debug
    for i in range(4, 0, -1):
        U[j+1][i] = alpha[j][i] * U[j+1][i+1] + beta[j][i]
        #print (alpha[j][i], beta[j][i]) debug

for row in U:
    print(" ".join(f"{val:.3f}" for val in row))