import math
m, l, h, lamda, c, p = 3, 0.5, 0.1, 35.1, 0.127, 11350
T1, T2 = 4, 160
a_1 = 1/4
a_0 = lamda/(c*p)
l_matrix = []
K = []
tau = 1/6
a = []
b = []
c = []
alpha=[[0 for i in range(5)] for j in range(3)]
beta=[[0 for i in range(5)] for j in range(3)]
F=[[0 for i in range(4)] for j in range(3)]
gamma = ( 1/2 * tau) / h**2
for i in range(0, 12, 2):
    l_matrix.append(i/10*l)

for i in range (0, 6):
    K.append(a_0*math.exp(-a_1*l_matrix[i]))

T=[[0 for i in range(6)] for j in range(4)] # 4 ... 160

for j in range (0, 4):
    T[j][0] = T1
for j in range (0, 4):
    T[j][5] = T2
for i in range(1, 5):
    T[0][i] = ((T2 - T1) / l ** 2 * l_matrix[i] ** 2 + T1)

for i in range(0, 4):
    a.append(1/2*(K[i]+K[i+1]))
    b.append(1 / 2 * (K[i+1] + K[i + 2]))
    c.append(a[i]+b[i]+1/gamma)

for j in range(0,3):
    alpha[j][0] = 0
    beta[j][0] = 4
    for i in range(4):
        alpha[j][i+1]=b[i]/(c[i]-a[i]*alpha[j][i])
        F[j][i]=-1*( -1/gamma * T[j][i+1] - b[i] * (T[j][i+2]-T[j][i+1]) + a[i]*(T[j][i+1]-T[j][i]))
        beta[j][i+1]=(a[i]*beta[j][i]+F[j][i])/(c[i]-a[i]*alpha[j][i])
    for i in range(4, 0, -1):
        T[j+1][i]=alpha[j][i]*T[j+1][i+1]+beta[j][i]
for row in T:
    print(" ".join(f"{val:.3f}" for val in row))
