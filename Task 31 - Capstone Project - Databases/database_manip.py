import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER,
        name TEXT,
        grade INTEGER
    )
""")
cur.execute("INSERT INTO python_programming VALUES (55, 'Carl Davis', 61)")
cur.execute("INSERT INTO python_programming VALUES (66, 'Dennis Fredrickson', 88)")
cur.execute("INSERT INTO python_programming VALUES (77, 'Jane Richards', 78)")
cur.execute("INSERT INTO python_programming VALUES (12, 'Peyton Sawyer', 45)")
cur.execute("INSERT INTO python_programming VALUES (2, 'Lucas Brooke', 99)")

cur.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
results = cur.fetchall()
print("Students with grades between 60 and 80:")
for row in results:
    print(row)

cur.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
cur.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
cur.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")
conn.commit()
conn.close()