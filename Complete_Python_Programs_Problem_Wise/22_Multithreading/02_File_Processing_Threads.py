"""
CONCEPT: 22 Multithreading
PROBLEM:
Process multiple files concurrently.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 File Processing Threads")
print("=" * 70)

import threading
import time

results = []
lock = threading.Lock()

def process_employee(employee_id, seconds):
    print(f"Thread started for {employee_id}")
    time.sleep(seconds)
    result = f"{employee_id} processed"
    with lock:
        results.append(result)
    print(f"Thread completed for {employee_id}")

employees = [
    ("EMP101", 1),
    ("EMP102", 2),
    ("EMP103", 1),
    ("EMP104", 2),
]

threads = []
start_time = time.time()

for employee_id, seconds in employees:
    thread = threading.Thread(
        target=process_employee,
        args=(employee_id, seconds)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

elapsed = time.time() - start_time

print("\nTHREADING REPORT")
for result in results:
    print(result)
print("Completed tasks:", len(results))
print(f"Elapsed time: {elapsed:.2f} seconds")
print("All worker threads have completed.")
