"""
CONCEPT: 23 Advanced Python
PROBLEM:
Process paired records using zip and enumerate.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("04 Zip Enumerate Project")
print("=" * 70)

employees = [
    {"id": "EMP101", "name": "Ravi", "salary": 65000},
    {"id": "EMP102", "name": "Anu", "salary": 72000},
    {"id": "EMP103", "name": "Kiran", "salary": 81000},
    {"id": "EMP104", "name": "Meena", "salary": 59000},
]

high_salary = [e for e in employees if e["salary"] >= 70000]
salary_map = {e["id"]: e["salary"] for e in employees}
names = [e["name"] for e in employees]
ids = [e["id"] for e in employees]

print("\nCOMPREHENSION REPORT")
print("High salary:", high_salary)
print("Salary map:", salary_map)
print("Names:", names)

print("\nZIP + ENUMERATE")
for index, (emp_id, name) in enumerate(zip(ids, names), start=1):
    print(index, emp_id, name)

original = {"employee": {"name": "Ravi", "skills": ["Python", "SQL"]}}
shallow = original.copy()
shallow["employee"]["skills"].append("Git")

print("\nCOPY DEMO")
print("Original:", original)
print("Shallow :", shallow)

first, *middle, last = employees
print("\nUNPACKING")
print("First:", first)
print("Middle:", middle)
print("Last:", last)
