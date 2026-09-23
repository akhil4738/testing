"""
CONCEPT: 17 Decorators
PROBLEM:
Implement role-based authorization using decorators.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("04 Authorization Decorator")
print("=" * 70)

from functools import wraps
from datetime import datetime

logged_in = True
user_role = "admin"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Access denied: login required.")
            return None
        return func(*args, **kwargs)
    return wrapper

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if user_role != "admin":
            print("Access denied: admin role required.")
            return None
        return func(*args, **kwargs)
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("LOG:", datetime.now(), "Calling", func.__name__)
        result = func(*args, **kwargs)
        print("LOG:", "Completed", func.__name__)
        return result
    return wrapper

@login_required
@admin_only
@logger
def generate_employee_report():
    print("\nEMPLOYEE REPORT")
    for i in range(1, 6):
        print(f"Employee {i}: report generated")
    return "SUCCESS"

result = generate_employee_report()
print("Result:", result)
print("Decorators applied: login check, role check and logging.")
