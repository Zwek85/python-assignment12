import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('db/lesson.db')

query = """
SELECT 
    e.employee_name AS last_name, 
    SUM(p.unit_price * l.quantity) AS revenue
FROM employee e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_item l ON o.order_id = l.order_id
JOIN product p ON l.product_id = p.product_id
GROUP BY e.employee_id, e.employee_name
ORDER BY revenue DESC;
"""

# Load data into DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Debug: print the results and datatypes
print("Employee Results:")
print(employee_results)
print("\nData types:")
print(employee_results.dtypes)

# Plotting if data exists and revenue is numeric
if not employee_results.empty and pd.api.types.is_numeric_dtype(employee_results['revenue']):
    employee_results.plot(
        kind='bar',
        x='last_name',
        y='revenue',
        color='skyblue',
        legend=False,
        figsize=(10, 6)
    )
    plt.title("Employee Revenue")
    plt.xlabel("Employee Last Name")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot or 'revenue' column is not numeric.")
