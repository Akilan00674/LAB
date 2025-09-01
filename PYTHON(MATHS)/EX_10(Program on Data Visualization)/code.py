import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate a hypothetical dataset
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value1': [25, 40, 30, 35, 20],
    'Value2': [15, 20, 25, 10, 30]
}
df = pd.DataFrame(data)

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Category'], df['Value1'])
plt.title('Bar Chart')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['Value2'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Value1'], df['Value2'], c='blue', marker='o')
plt.title('Scatter Plot')
plt.xlabel('Value1')
plt.ylabel('Value2')
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Value1'], bins=np.arange(15, 45, 5), edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value1')
plt.ylabel('Frequency')
plt.show()
