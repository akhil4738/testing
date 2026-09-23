"""
CONCEPT: 20 Math and Random
PROBLEM:
Build a number guessing game with attempts and score.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("03 Number Guessing Game")
print("=" * 70)

import math
import random

print("\nNUMBER GAME")
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower >= upper:
    print("Lower limit must be smaller than upper limit.")
else:
    secret = random.randint(lower, upper)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        attempts += 1

        if guess == secret:
            print("Correct! Attempts used:", attempts)
            break
        elif guess < secret:
            print("Hint: Try a higher number.")
        else:
            print("Hint: Try a lower number.")
    else:
        print("Game over. Secret number was:", secret)

    width = upper - lower
    print("\nMATH DETAILS")
    print("Range width:", width)
    print("Square root of upper:", math.sqrt(upper))
    print("Power:", math.pow(upper, 2))
    print("Ceiling average:", math.ceil((lower + upper) / 2))
    print("Floor average:", math.floor((lower + upper) / 2))
