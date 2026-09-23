"""
CONCEPT: 21 SQLite Database
PROBLEM:
Store sales and generate summary reports using SQL queries.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Sales Database Project")
print("=" * 70)

import sqlite3

connection = sqlite3.connect("training_company.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

cursor.execute("SELECT COUNT(*) FROM employees")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)",
        [
            ("Ravi", "Python", 65000),
            ("Anu", "Java", 72000),
            ("Kiran", "Data", 81000),
            ("Meena", "Testing", 59000)
        ]
    )

connection.commit()

print("\nEMPLOYEE DATABASE")
rows = cursor.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY salary DESC"
).fetchall()

for row in rows:
    print(row)

minimum = float(input("\nEnter minimum salary: "))
rows = cursor.execute(
    "SELECT name, department, salary FROM employees WHERE salary >= ?",
    (minimum,)
).fetchall()

print("\nFILTERED EMPLOYEES")
for row in rows:
    print(row)

summary = cursor.execute(
    "SELECT COUNT(*), SUM(salary), AVG(salary) FROM employees"
).fetchone()

print("Count:", summary[0])
print("Total payroll:", summary[1])
print("Average salary:", summary[2])

connection.close()
print("Database connection closed.")
