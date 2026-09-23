"""
CONCEPT: 08 Tuples
PROBLEM:
Validate tuple-based records and separate valid and invalid entries.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Tuple Data Validation")
print("=" * 70)

records = (
    ("EMP101", "Ravi", "Python", 72000),
    ("EMP102", "Anu", "Java", 68000),
    ("EMP103", "Kiran", "Data", 81000),
    ("EMP104", "Meena", "Testing", 59000),
)

print("\nEMPLOYEE TUPLE REPORT")
print("-" * 55)
for record in records:
    emp_id, name, department, salary = record
    print(f"{emp_id:8} {name:10} {department:12} {salary:10.2f}")

search_id = input("\nEnter employee ID to search: ").strip().upper()
found = False
for record in records:
    if record[0] == search_id:
        print("Employee found:")
        print("ID:", record[0])
        print("Name:", record[1])
        print("Department:", record[2])
        print("Salary:", record[3])
        found = True
        break

if not found:
    print("Employee not found.")

salaries = tuple(record[3] for record in records)
print("Total salary:", sum(salaries))
print("Average salary:", sum(salaries) / len(salaries))
print("Highest salary:", max(salaries))
