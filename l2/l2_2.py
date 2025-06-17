#система с неограниченным ожиданием
#задача из тетради
L = 7
M = 1
X = 10

RO = L/M

F = 1
R = 1
S = 1

for i in range(1,X+1):
    F = F * i
    R = R * RO
    S = S + R/F
S = S + (R * RO)/(F * (X - RO))
P0 = 1/S
Y1 = (R * RO * P0)/((F/X)*(X-RO)*(X-RO))
Y2 = Y1 + RO
Y3 = Y1/L
Y4 = Y2/L
print("Y1 =")
print(Y1)
print("Y2 =")
print(Y2)
print("Y3 =")
print(Y3)
print("Y4 =")
print(Y4)