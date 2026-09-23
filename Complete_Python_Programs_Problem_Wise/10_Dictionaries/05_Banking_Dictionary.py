"""
CONCEPT: 10 Dictionaries
PROBLEM:
Create a simple account manager using dictionaries for deposit, withdrawal and balance checks.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Banking Dictionary")
print("=" * 70)

employees = {
    "EMP101": {"name": "Ravi", "department": "Python", "salary": 65000},
    "EMP102": {"name": "Anu", "department": "Java", "salary": 72000},
    "EMP103": {"name": "Kiran", "department": "Data", "salary": 81000},
}

print("\nEMPLOYEE DATABASE")
for emp_id, data in employees.items():
    print(f"{emp_id} -> {data}")

search_id = input("\nEnter employee ID: ").strip().upper()
if search_id in employees:
    data = employees[search_id]
    print("Name:", data["name"])
    print("Department:", data["department"])
    print("Salary:", data["salary"])
else:
    print("Employee not found.")

new_id = input("\nEnter a new employee ID: ").strip().upper()
if new_id:
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))
    employees[new_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }

print("\nUPDATED DATABASE")
total = 0
for emp_id, data in employees.items():
    total += data["salary"]
    print(emp_id, data)
print("Total payroll:", total)
print("Average payroll:", total / len(employees))
