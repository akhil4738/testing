"""
CONCEPT: 12 Modules and Packages
PROBLEM:
Build an employee joining-date and experience calculator using datetime.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 Date Module Project")
print("=" * 70)

import math
from datetime import datetime, date

print("\nMODULE DEMONSTRATION PROJECT")
amount = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
years = float(input("Enter years: "))

simple_interest = amount * rate * years / 100
monthly_rate = rate / 1200
months = int(years * 12)

if monthly_rate > 0:
    emi = amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
else:
    emi = amount / months

print("Principal       :", amount)
print("Rate            :", rate)
print("Years           :", years)
print("Simple interest :", simple_interest)
print("Estimated EMI   :", round(emi, 2))
print("Square root     :", math.sqrt(amount))
print("Today           :", date.today())
print("Current time    :", datetime.now().strftime("%H:%M:%S"))
print("This program demonstrates reusable standard-library modules.")
