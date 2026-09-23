"""
CONCEPT: 18 Regular Expressions
PROBLEM:
Extract IDs, amounts and dates from semi-structured text.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Data Extractor")
print("=" * 70)

import re

text = """
Contact ravi@example.com or anil@test.org.
Phone: +91-9876543210.
Ticket IDs: INC-1023, INC-2045.
Amount: Rs. 45,500.
Date: 23-09-2026.
"""

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phones = re.findall(r"(?:\+91[- ]?)?[6-9]\d{9}", text)
tickets = re.findall(r"INC-\d+", text)
amounts = re.findall(r"Rs\.\s?[\d,]+", text)
dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)

print("\nREGEX EXTRACTION REPORT")
print("Emails :", emails)
print("Phones :", phones)
print("Tickets:", tickets)
print("Amounts:", amounts)
print("Dates  :", dates)

email_to_check = input("\nEnter email to validate: ").strip()
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
print("Valid email:", bool(re.fullmatch(email_pattern, email_to_check)))
print("Regular expressions are useful for structured text validation and extraction.")
