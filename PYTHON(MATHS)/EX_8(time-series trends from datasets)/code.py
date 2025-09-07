import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Akilan\cloud\PYTHON(MATHS)\EX_8(time-series trends from datasets)\covid.csv", 
                 parse_dates=['Date'], index_col='Date')
df['Cases'].plot(label='Daily Cases')

df['Cases'].rolling(7).mean().plot(label='7-Day Average')

plt.legend()
plt.title("COVID-19 Trend")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.grid(True)
plt.show()
