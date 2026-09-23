"""
CONCEPT: 14 File Handling
PROBLEM:
Analyze a log file for error, warning and information counts.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("03 Log File Analyzer")
print("=" * 70)

from pathlib import Path
import json

file_name = "employee_records.json"

records = [
    {"id": "EMP101", "name": "Ravi", "department": "Python", "salary": 65000},
    {"id": "EMP102", "name": "Anu", "department": "Java", "salary": 72000},
    {"id": "EMP103", "name": "Kiran", "department": "Data", "salary": 81000},
]

path = Path(file_name)
path.write_text(json.dumps(records, indent=4), encoding="utf-8")

print("File created:", path.resolve())

data = json.loads(path.read_text(encoding="utf-8"))
print("\nEMPLOYEE RECORDS")
for employee in data:
    print(employee["id"], employee["name"], employee["department"], employee["salary"])

minimum = float(input("\nEnter minimum salary: "))
filtered = [e for e in data if e["salary"] >= minimum]

print("\nFILTERED REPORT")
for employee in filtered:
    print(f'{employee["id"]}: {employee["name"]} -> {employee["salary"]}')

total = sum(e["salary"] for e in data)
print("Total payroll:", total)
print("Average salary:", total / len(data))
print("Records saved safely in JSON format.")
