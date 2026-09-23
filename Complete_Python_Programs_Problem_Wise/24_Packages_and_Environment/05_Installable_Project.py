"""
CONCEPT: 24 Packages and Environment
PROBLEM:
Prepare a small package project with metadata and reusable code.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("05 Installable Project")
print("=" * 70)

from pathlib import Path
import sys

project = Path("python_training_project")
folders = [
    project / "app",
    project / "tests",
    project / "data",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

requirements = project / "requirements.txt"
requirements.write_text(
    "# Add third-party packages used by the project\n",
    encoding="utf-8"
)

readme = project / "README.md"
readme.write_text(
    "# Python Training Project\n\n"
    "Create a virtual environment before installing packages.\n",
    encoding="utf-8"
)

print("\nPROJECT STRUCTURE CREATED")
for path in project.rglob("*"):
    print(path)

print("\nPython executable:", sys.executable)
print("Python version:", sys.version)
print("Recommended workflow:")
print("1. Create virtual environment")
print("2. Activate it")
print("3. Install requirements")
print("4. Run tests")
print("5. Run application")
