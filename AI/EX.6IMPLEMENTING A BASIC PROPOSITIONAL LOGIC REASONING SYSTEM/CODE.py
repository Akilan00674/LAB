from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent

# Define propositional variables
A, B, C = symbols('A B C')

# Assign truth values
truth_values = {
    A: True,
    B: False,
    C: True
}

# Define expressions
expr1 = And(A, Not(C))            # A ∧ ¬C
expr2 = And(Or(A, B), C)          # (A ∨ B) ∧ C
expr3 = Or(Not(B), A)             # ¬B ∨ A
expr4 = Implies(A, C)             # A → C
expr5 = Equivalent(B, C)          # B ↔ C

# Evaluation function
def evaluate_expression(expr, truth_vals):
    return expr.subs(truth_vals)

# Display results
print("\n--- Evaluating Propositional Logic Expressions using SymPy ---")
print(f"A ∧ ¬C = {evaluate_expression(expr1, truth_values)}")
print(f"(A ∨ B) ∧ C = {evaluate_expression(expr2, truth_values)}")
print(f"¬B ∨ A = {evaluate_expression(expr3, truth_values)}")
print(f"A → C = {evaluate_expression(expr4, truth_values)}")
print(f"B ↔ C = {evaluate_expression(expr5, truth_values)}")
