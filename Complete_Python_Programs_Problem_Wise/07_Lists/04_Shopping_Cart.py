"""
CONCEPT: 07 Lists
PROBLEM:
Build a shopping cart using lists with quantities, prices, discounts and final bill.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("04 Shopping Cart")
print("=" * 70)

count = int(input("How many products/students? "))
records = []
for i in range(count):
    name = input(f"Enter name {i + 1}: ").strip()
    value = float(input(f"Enter amount/marks for {name}: "))
    records.append([name, value])

print("\nRECORDS")
for record in records:
    print(f"{record[0]:20} {record[1]:10.2f}")

values = [record[1] for record in records]
if values:
    average = sum(values) / len(values)
    highest = max(values)
    lowest = min(values)
    print("-" * 35)
    print(f"Average : {average:.2f}")
    print(f"Highest : {highest:.2f}")
    print(f"Lowest  : {lowest:.2f}")

    above = [record[0] for record in records if record[1] > average]
    print("Above average:", above)
else:
    print("No records entered.")

print("List processing completed.")
