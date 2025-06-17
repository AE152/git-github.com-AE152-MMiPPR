L = 10
M = 7
X = 1

RO = L/M

Potk  = 1
while (Potk > 0.1):
    X += 1
    F = 1
    R = 1
    S = 1
    
    for i in range(1,X+1):
        F = F * i
        R = R * RO
        S = S + R/F
    P0 = 1/S
    Potk = (R/F) * P0

print("P0 = ", str(P0))
print("Potk = ", str(Potk))
print("X = ", str(X))
