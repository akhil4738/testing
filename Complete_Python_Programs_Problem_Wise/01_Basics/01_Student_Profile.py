"""
CONCEPT: 01 Basics
PROBLEM:
Create a student profile program that accepts name, age, course, college and marks, then prints a formatted report.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("01 Student Profile")
print("=" * 70)

name = input("Enter employee/student name: ").strip()
age = int(input("Enter age: "))
course = input("Enter course/designation: ").strip()
city = input("Enter city: ").strip()
marks = float(input("Enter percentage/score: "))

status = "Eligible" if marks >= 50 else "Needs Improvement"
print("\nPROFILE REPORT")
print("-" * 40)
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Course/Job : {course}")
print(f"City       : {city}")
print(f"Score      : {marks:.2f}")
print(f"Status     : {status}")
print("-" * 40)
print("Record created successfully.")
print("Next step: extend this program for multiple records.")
