import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Akilan/cloud/PYTHON(MATHS)/EX_7(Sales Data Analysis)/sales.csv")

# Fill missing values with 0
df.fillna(0, inplace=True)

# Create pivot table to summarize sales by region
report = df.pivot_table(index='Region', values='Sales', aggfunc='sum')

# Display report
print("\n--- Sales Report by Region ---")
print(report)
