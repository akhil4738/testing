"""
CONCEPT: 25 Mini Projects
PROBLEM:
Build an inventory application with stock operations and low-stock reports.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("04 Inventory Management System")
print("=" * 70)

from collections import defaultdict

records = [
    {"id": "EMP101", "name": "Ravi", "department": "Python", "salary": 65000},
    {"id": "EMP102", "name": "Anu", "department": "Java", "salary": 72000},
    {"id": "EMP103", "name": "Kiran", "department": "Data", "salary": 81000},
    {"id": "EMP104", "name": "Meena", "department": "Python", "salary": 59000},
]

def display_menu():
    print("\nEMPLOYEE MANAGEMENT")
    print("1. Display employees")
    print("2. Search employee")
    print("3. Department summary")
    print("4. Highest salary")
    print("5. Exit")

def display_employees(data):
    for employee in data:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )

def search_employee(data, emp_id):
    for employee in data:
        if employee["id"] == emp_id:
            return employee
    return None

def department_summary(data):
    summary = defaultdict(float)
    for employee in data:
        summary[employee["department"]] += employee["salary"]
    return summary

while True:
    display_menu()
    choice = input("Enter choice: ").strip()

    if choice == "1":
        display_employees(records)
    elif choice == "2":
        emp_id = input("Enter employee ID: ").strip().upper()
        employee = search_employee(records, emp_id)
        print(employee if employee else "Employee not found.")
    elif choice == "3":
        summary = department_summary(records)
        for department, total in summary.items():
            print(department, total)
    elif choice == "4":
        highest = max(records, key=lambda e: e["salary"])
        print("Highest salary:", highest)
    elif choice == "5":
        print("Application closed.")
        break
    else:
        print("Invalid choice. Try again.")
