import pandas as pd
import matplotlib.pyplot as plt

# Read COVID dataset (with Date column as index)
df = pd.read_csv(r"C:\Users\Akilan\cloud\PYTHON(MATHS)\EX_8(time-series trends from datasets)\covid.csv", 
                 parse_dates=['Date'], index_col='Date')
# Plot actual daily cases
df['Cases'].plot(label='Daily Cases')

# Plot rolling 7-day average for smoothing
df['Cases'].rolling(7).mean().plot(label='7-Day Average')

# Add legend and title
plt.legend()
plt.title("COVID-19 Trend")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.grid(True)
plt.show()
