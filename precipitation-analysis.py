import matplotlib.pyplot as plt
import pandas as pd

# Load CSV data
df = pd.read_csv('precip-data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter year
year_to_plot = int(input("Enter the year to plot (e.g., 2020): "))
df = df[df['Date'].dt.year == year_to_plot]

# Plot Data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['PRCP (Inches)'], label="Precipitation", color='blue')
plt.plot(df['Date'], df['SNOW (Inches)'], label="Snow", color='black')
plt.title('Daily Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (inches)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()