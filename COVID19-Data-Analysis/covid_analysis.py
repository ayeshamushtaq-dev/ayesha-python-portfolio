import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv")

# Filter for a specific country
pakistan_data = df[df['Country'] == 'Pakistan']

# Plot time series
plt.figure(figsize=(10, 5))
plt.plot(pakistan_data['Date'], pakistan_data['Confirmed'], label='Confirmed Cases')
plt.plot(pakistan_data['Date'], pakistan_data['Deaths'], label='Deaths')
plt.title("COVID-19 Trend in Pakistan")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
