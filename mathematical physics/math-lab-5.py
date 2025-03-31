import math
m, l, n, h, tau, a_0 = 4, 1, 5, 0.2, 1, 10
U=[[0 for i in range(6)] for j in range(4)]
l_matrix = []
mu = []
r_plus = []
r_minus = []
a = []
b = []
c = []
alpha=[[0 for i in range(6)] for j in range(3)]
beta=[[0 for i in range(6)] for j in range(3)]
for i in range(0, 6):
    l_matrix.append(i/10*2)
    mu.append(1/(1+1/2*h*abs(m*math.cos(math.pi*l_matrix[i]))))
    r_plus.append((((4 * math.cos(math.pi * l_matrix[i])) + abs(4 * math.cos(math.pi * l_matrix[i])))) / 2)
    r_minus.append((((4 * math.cos(math.pi * l_matrix[i])) - abs(4 * math.cos(math.pi * l_matrix[i])))) / 2)
    a.append(mu[i]/h**2-r_minus[i]/h)
    b.append(mu[i]/h**2+r_plus[i]/h)
    c.append((2*mu[i])/h**2+1+r_plus[i]/h-r_minus[i]/h)
for i in range(0, 4):
    U[i][0] = a_0
    U[i][5] =10*math.exp(-1*m)
for j in range(1, 5):
    U[0][j] = 10*math.exp(-1*m*l_matrix[j])

for j in range(0,3):
    alpha[j][0] = 0
    beta[j][0] = 10
    for i in range(5):
        alpha[j][i+1]=b[i]/(c[i]-a[i]*alpha[j][i])
        beta[j][i+1]=(a[i]*beta[j][i]+U[j][i])/(c[i]-a[i]*alpha[j][i])
        #print(beta[j][i+1], U[j][i])
    for i in range(4, 0, -1):
        U[j+1][i]=alpha[j][i+1]*U[j+1][i+1]+beta[j][i+1]
        #print(j+1, i, U[j+1][i], alpha[j][i+1], beta[j][i+1])


for row in U:
    print(" ".join(f"{val:.3f}" for val in row))