import numpy as np

def input_matrix(name):
    rows = int(input(f"\nEnter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(f"{name}[{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

# Input matrices
print("===== MATRIX OPERATIONS =====")
A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

# Display original matrices
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# Try addition and subtraction only if shapes match
if A.shape == B.shape:
    print("\nAddition (A + B):\n", np.add(A, B))
    print("Subtraction (A - B):\n", np.subtract(A, B))
else:
    print("\nAddition/Subtraction not possible (shapes differ):")
    print(f"A shape: {A.shape}, B shape: {B.shape}")

# Transpose
print("\nTranspose of A:\n", np.transpose(A))
print("Transpose of B:\n", np.transpose(B))

# Multiplication if inner dimensions match
if A.shape[1] == B.shape[0]:
    print("\nMultiplication (A x B):\n", np.matmul(A, B))
else:
    print("\nMultiplication not possible: A columns != B rows.")
