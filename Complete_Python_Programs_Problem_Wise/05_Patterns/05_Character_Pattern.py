"""
CONCEPT: 05 Patterns
PROBLEM:
Generate an alphabet pattern using nested loops and character arithmetic.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Character Pattern")
print("=" * 70)

rows = int(input("Enter number of rows: "))
if rows < 1:
    print("Rows must be positive.")
else:
    print("\nPATTERN")
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        values = ""
        for j in range(1, i + 1):
            values += str(j) + " "
        print(spaces + values)

    print("\nREVERSE")
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        values = ""
        for j in range(1, i + 1):
            values += str(j) + " "
        print(spaces + values)

    print("\nPattern generated using nested loops.")
