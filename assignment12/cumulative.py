import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('db/lesson.db')

query = """
SELECT 
    o.order_id,
    SUM(p.unit_price * l.quantity) AS total_price
FROM orders o
JOIN line_item l ON o.order_id = l.order_id
JOIN product p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Make sure total_price is numeric
df['total_price'] = pd.to_numeric(df['total_price'], errors='coerce')

# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs order_id
df.plot(
    kind='line',
    x='order_id',
    y='cumulative',
    color='green',
    marker='o',
    title='Cumulative Revenue by Order ID',
    legend=False,
    figsize=(10, 6)
)

plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()
