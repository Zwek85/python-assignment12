import sqlite3

conn = sqlite3.connect('db/lesson.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(line_item);")
columns = cursor.fetchall()

print("Columns in 'line_item' table:")
for col in columns:
    print(col)
