"""
CONCEPT: 02 Operators
PROBLEM:
Accept principal, annual interest and tenure; calculate monthly interest, total interest and payment estimates.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 Loan EMI Components")
print("=" * 70)

amount = float(input("Enter original amount: "))
quantity = int(input("Enter quantity: "))
discount_rate = float(input("Enter discount percentage: "))
tax_rate = float(input("Enter tax percentage: "))
fixed_charge = float(input("Enter fixed charge: "))

subtotal = amount * quantity
discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
final_amount = after_discount + tax + fixed_charge

print("\nCALCULATION REPORT")
print(f"Unit amount       : {amount:.2f}")
print(f"Quantity          : {quantity}")
print(f"Subtotal          : {subtotal:.2f}")
print(f"Discount          : {discount:.2f}")
print(f"After discount    : {after_discount:.2f}")
print(f"Tax               : {tax:.2f}")
print(f"Fixed charge      : {fixed_charge:.2f}")
print(f"Final amount      : {final_amount:.2f}")
print(f"Discount saved    : {discount:.2f}")
print(f"Tax percentage    : {tax_rate:.2f}%")
