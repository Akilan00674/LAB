import numpy as np

# Step 1: Get the number of equations (which equals number of variables)
n = int(input("Enter number of variables (and equations): "))

# Step 2: Initialize empty lists to store coefficients and constants
A = []  # Coefficient matrix
B = []  # Constant vector

print("\nEnter coefficients and constants for each equation:")

# Step 3: Loop to get input for each equation
for i in range(n):
    row = [float(x) for x in input(f"Enter coefficients of equation {i+1} (space-separated): ").split()]
    const = float(input(f"Enter constant term of equation {i+1}: "))
    A.append(row)
    B.append(const)

# Step 4: Convert lists to NumPy arrays
A = np.array(A)
B = np.array(B)

# Step 5: Solve the system of equations
X = np.linalg.solve(A, B)

# Step 6: Print the solution
print("\nSolution:")
for i in range(n):
    print(f"x{i+1} = {X[i]:.4f}")
