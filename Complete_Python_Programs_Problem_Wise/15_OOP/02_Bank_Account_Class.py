"""
CONCEPT: 15 OOP
PROBLEM:
Build a BankAccount class supporting deposit, withdrawal, transfer and transaction history.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 Bank Account Class")
print("=" * 70)

class Employee:
    company = "Tech Solutions"

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def apply_increment(self, percentage):
        self.salary += self.salary * percentage / 100

    def display(self):
        print(f"ID         : {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Monthly    : {self.salary:.2f}")
        print(f"Annual     : {self.annual_salary():.2f}")

employees = [
    Employee("EMP101", "Ravi", "Python", 65000),
    Employee("EMP102", "Anu", "Java", 72000),
    Employee("EMP103", "Kiran", "Data", 81000),
]

for employee in employees:
    employee.display()
    print("-" * 40)

percentage = float(input("Enter increment percentage: "))
for employee in employees:
    employee.apply_increment(percentage)

print("\nAFTER INCREMENT")
for employee in employees:
    employee.display()
    print("-" * 40)

print("Company:", Employee.company)
print("OOP concepts used: class, object, constructor, method, class variable.")
