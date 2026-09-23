"""
CONCEPT: 11 Functions
PROBLEM:
Demonstrate positional, keyword, default and variable-length arguments in a practical billing system.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Function Arguments Project")
print("=" * 70)

def calculate_total(values):
    return sum(values)

def calculate_average(values):
    return calculate_total(values) / len(values) if values else 0

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"

def create_report(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    return {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }

name = input("Enter student name: ")
count = int(input("Enter number of subjects: "))
marks = []

for i in range(count):
    marks.append(float(input(f"Enter mark {i + 1}: ")))

report = create_report(name, marks)

print("\nRESULT REPORT")
print("Name    :", report["name"])
print("Marks   :", marks)
print("Total   :", report["total"])
print("Average :", f'{report["average"]:.2f}')
print("Grade   :", report["grade"])
print("Functions used:", "calculate_total, calculate_average, calculate_grade, create_report")
