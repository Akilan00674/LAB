import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    'Hours_Studied': [5, 3, 8, 2, 7, 4],
    'Attendance': [1, 1, 1, 0, 1, 0],
    'Passed': [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['Hours_Studied', 'Attendance']]
y = df['Passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\n--- Predict Student Performance ---")

try:
    hrs = float(input("Enter hours studied: "))
    att = int(input("Enter attendance (1 for Present, 0 for Absent): "))

    user_input = pd.DataFrame([[hrs, att]], columns=['Hours_Studied', 'Attendance'])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        print("Prediction: The student is likely to PASS.")
    else:
        print("Prediction: The student is likely to FAIL.")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
 # type: ignore