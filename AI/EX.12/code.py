import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load local CSV (make sure path is correct)
data = pd.read_csv(r"C:\Users\Akilan\cloud\AI\EX.12\student.csv", sep=';')

# Show first 5 rows
print(data.head())

# Create binary target column 'pass' (1 = pass, 0 = fail)
data['pass'] = data['G3'] >= 10
data['pass'] = data['pass'].astype(int)

# Select features
features = ['studytime', 'failures', 'absences']
X = data[features]
y = data['pass']

# Split into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature importance
importance = model.feature_importances_

# Plot feature importance
sns.barplot(x=features, y=importance)
plt.title("Feature Importance for Student Performance Prediction")
plt.show()
