"""
CONCEPT: 19 Dates and Time
PROBLEM:
Calculate employee experience from joining date.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("01 Employee Experience")
print("=" * 70)

from datetime import datetime, date

dob_text = input("Enter date of birth (DD-MM-YYYY): ").strip()
joining_text = input("Enter joining date (DD-MM-YYYY): ").strip()

dob = datetime.strptime(dob_text, "%d-%m-%Y").date()
joining = datetime.strptime(joining_text, "%d-%m-%Y").date()
today = date.today()

age_days = (today - dob).days
experience_days = (today - joining).days

age_years = age_days // 365
experience_years = experience_days // 365
experience_months = (experience_days % 365) // 30

print("\nDATE REPORT")
print("Today             :", today.strftime("%d-%m-%Y"))
print("Date of birth     :", dob.strftime("%d-%m-%Y"))
print("Joining date      :", joining.strftime("%d-%m-%Y"))
print("Approx age        :", age_years, "years")
print("Experience        :", experience_years, "years", experience_months, "months")
print("Days since DOB    :", age_days)
print("Days since joining:", experience_days)

deadline_text = input("Enter project deadline (DD-MM-YYYY): ").strip()
deadline = datetime.strptime(deadline_text, "%d-%m-%Y").date()
remaining = (deadline - today).days
print("Days until deadline:", remaining)
