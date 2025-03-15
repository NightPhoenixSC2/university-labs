k, s, l, h, m, p, lamda, c, T1, T2 = 4, 1, 0.5, 0.1, 3, 11350, 35.1, 0.127, 4, 160
Tx0=(T2-T1)/l**2*1+T1
aa=lamda/(c*p)
tau1=1/6*h**2/aa
l_matrix = []
ksi=aa*tau1/h**2

for i in range(2, 12, 2): # 0.1, 0.2, 0.3, 0.4, 0.5
    l_matrix.append(i/10*l)

T=[[0 for i in range(6)] for j in range(4)]
for j in range (0, 4):
    T[j][0] = T1
for j in range (0, 4):
    T[j][5] = T2
for i in range(1, 5):
    T[0][i] = ((T2 - T1) / l ** 2 * l_matrix[i - 1] ** 2 + T1) # T0

for j in range (1, 4):
    for i in range(1, 5):
        T[j][i] = (1-2*ksi)*T[j-1][i]+ksi*(T[j-1][i-1]+T[j-1][i+1])

for row in T:
    print(" ".join(f"{val:.3f}" for val in row))