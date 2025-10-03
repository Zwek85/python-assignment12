import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# Clean the 'strength' column:
# It looks like strength might have some non-numeric chars, so remove them using regex
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True)

# Convert strength to float
df['strength'] = df['strength'].astype(float)

# Create an interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength': 'Strength', 'frequency': 'Frequency'}
)

# Save the plot to an HTML file
fig.write_html("wind.html")


print("Plot saved as wind.html")
