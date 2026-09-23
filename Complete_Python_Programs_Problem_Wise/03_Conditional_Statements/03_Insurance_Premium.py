"""
CONCEPT: 03 Conditional Statements
PROBLEM:
Calculate insurance premium based on age, vehicle type, claim history and coverage.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("03 Insurance Premium")
print("=" * 70)

salary = float(input("Enter monthly salary: "))
experience = float(input("Enter years of experience: "))
rating = float(input("Enter performance rating (1-5): "))
credit_score = int(input("Enter credit score: "))

if rating >= 4.5:
    appraisal = 15
elif rating >= 4:
    appraisal = 10
elif rating >= 3:
    appraisal = 6
else:
    appraisal = 0

if experience >= 5 and rating >= 4:
    bonus = salary * 0.10
elif experience >= 2 and rating >= 3:
    bonus = salary * 0.05
else:
    bonus = 0

revised_salary = salary + salary * appraisal / 100
eligible = credit_score >= 700 and salary >= 25000

print("\nDECISION REPORT")
print(f"Appraisal rate : {appraisal}%")
print(f"Appraisal      : {salary * appraisal / 100:.2f}")
print(f"Bonus          : {bonus:.2f}")
print(f"Revised salary : {revised_salary:.2f}")
print(f"Loan eligible  : {'YES' if eligible else 'NO'}")
print("Review the conditions and modify the rules for your organization.")
