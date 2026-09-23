"""
CONCEPT: 04 Loops
PROBLEM:
Process attendance for several employees and produce individual attendance percentages and eligibility.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 Employee Attendance")
print("=" * 70)

count = int(input("How many values/students/employees? "))
values = []
for i in range(count):
    value = float(input(f"Enter value {i + 1}: "))
    values.append(value)

total = 0
even_count = 0
odd_count = 0
positive = 0
negative = 0

for value in values:
    total += value
    if value >= 0:
        positive += 1
    else:
        negative += 1
    if value.is_integer() and int(value) % 2 == 0:
        even_count += 1
    elif value.is_integer():
        odd_count += 1

average = total / count if count else 0
maximum = max(values) if values else 0
minimum = min(values) if values else 0

print("\nLOOP ANALYSIS REPORT")
print(f"Values       : {values}")
print(f"Total        : {total:.2f}")
print(f"Average      : {average:.2f}")
print(f"Maximum      : {maximum:.2f}")
print(f"Minimum      : {minimum:.2f}")
print(f"Positive     : {positive}")
print(f"Negative     : {negative}")
print(f"Even integers: {even_count}")
print(f"Odd integers : {odd_count}")
print("Loop processing completed.")
