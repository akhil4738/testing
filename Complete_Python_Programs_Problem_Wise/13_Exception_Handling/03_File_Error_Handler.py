"""
CONCEPT: 13 Exception Handling
PROBLEM:
Handle missing files, permission errors and invalid content.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("03 File Error Handler")
print("=" * 70)

balance = 50000.0

def read_amount():
    try:
        amount = float(input("Enter transaction amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError as error:
        print("Invalid amount:", error)
        return None

print("\nBANK TRANSACTION")
try:
    amount = read_amount()
    if amount is not None:
        operation = input("Enter D for deposit or W for withdrawal: ").strip().upper()

        if operation == "D":
            balance += amount
            print("Deposit successful.")
        elif operation == "W":
            if amount > balance:
                raise RuntimeError("Insufficient balance.")
            balance -= amount
            print("Withdrawal successful.")
        else:
            raise ValueError("Unknown transaction type.")

except RuntimeError as error:
    print("Transaction error:", error)
except ValueError as error:
    print("Input error:", error)
except Exception as error:
    print("Unexpected error:", error)
else:
    print("Transaction completed without exception.")
finally:
    print(f"Available balance: {balance:.2f}")
    print("Transaction processing finished.")
