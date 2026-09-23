"""
CONCEPT: 16 Iterators Generators
PROBLEM:
Generate reports lazily from a sequence of records.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Generator Report")
print("=" * 70)

class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.employees):
            raise StopIteration
        employee = self.employees[self.index]
        self.index += 1
        return employee

def salary_generator(employees, minimum):
    for employee in employees:
        if employee["salary"] >= minimum:
            yield employee

employees = [
    {"id": "EMP101", "name": "Ravi", "salary": 65000},
    {"id": "EMP102", "name": "Anu", "salary": 72000},
    {"id": "EMP103", "name": "Kiran", "salary": 81000},
]

print("\nCUSTOM ITERATOR")
iterator = EmployeeIterator(employees)
for employee in iterator:
    print(employee)

minimum = float(input("\nMinimum salary for generator: "))
print("\nGENERATOR OUTPUT")
count = 0
for employee in salary_generator(employees, minimum):
    print(employee)
    count += 1

print("Matching employees:", count)
print("Generators produce values lazily instead of building another full collection.")
