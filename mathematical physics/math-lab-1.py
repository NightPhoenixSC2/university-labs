x1 = 8
x2 = 210
k1 = (x2-x1)/4
k2 = 8
epsilon = 0.1

f = []

for i in range(1,4):
    f.append(k1*i+k2)

print(f)

T = [[0 for i in range(2)] for j in range(3)]
T[0][0] = T[0][1] = (x1+x2+f[0]+f[0])/4
T[1][0] = T[1][1] = (x1+x2+f[1]+f[1])/4
T[2][0] = T[2][1] = (x1+x2+f[2]+f[2])/4
print(f"{T[0][0]:.4f} {T[0][1]:.4f} {T[1][0]:.4f} {T[1][1]:.4f} {T[2][0]:.4f} {T[2][1]:.4f}")


while True:
    T_prev = [row[:] for row in T]  # Copy the previous values of T

    T[0][0] = (x1 + f[0] + T_prev[1][0] + T_prev[0][1]) / 4
    T[0][1] = (x1 + f[0] + T_prev[0][0] + T_prev[1][1]) / 4

    T[1][0] = (T_prev[0][0] + f[1] + T_prev[1][1] + T_prev[2][0]) / 4
    T[1][1] = (T_prev[0][1] + f[1] + T_prev[1][0] + T_prev[2][1]) / 4

    T[2][0] = (T_prev[1][0] + f[2] + x2 + T_prev[2][1]) / 4
    T[2][1] = (T_prev[1][1] + f[2] + x2 + T_prev[2][0]) / 4

    print(f"{T[0][0]:.3f} {T[0][1]:.3f} {T[1][0]:.3f} {T[1][1]:.3f} {T[2][0]:.3f} {T[2][1]:.3f}")

    if all(abs(T[i][j] - T_prev[i][j]) < epsilon for i in range(3) for j in range(2)):
        break

print("\nТочність")
for i in range(3):
    for j in range(2):
        print(f"{abs(T[i][j] - T_prev[i][j]):.3f}", end=" ")