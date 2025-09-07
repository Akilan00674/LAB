import numpy as np

n = int(input("Enter number of variables (and equations): "))

A = []  
B = []  

print("\nEnter coefficients and constants for each equation:")

for i in range(n):
    row = [float(x) for x in input(f"Enter coefficients of equation {i+1} (space-separated): ").split()]
    const = float(input(f"Enter constant term of equation {i+1}: "))
    A.append(row)
    B.append(const)

A = np.array(A)
B = np.array(B)

X = np.linalg.solve(A, B)

print("\nSolution:")
for i in range(n):
    print(f"x{i+1} = {X[i]:.4f}")
