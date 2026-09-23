"""
CONCEPT: 09 Sets
PROBLEM:
Use sets to audit duplicate IDs across multiple data sources.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("04 Duplicate Data Audit")
print("=" * 70)

python_skills = {"Python", "SQL", "Git", "Flask", "Django"}
java_skills = {"Java", "SQL", "Git", "Spring", "Hibernate"}
required = {"Python", "SQL", "Git", "Flask"}

print("Python team skills:", python_skills)
print("Java team skills   :", java_skills)
print("Required skills    :", required)

common = python_skills & java_skills
python_only = python_skills - java_skills
all_skills = python_skills | java_skills
missing = required - python_skills

print("\nSET ANALYSIS")
print("Common skills :", common)
print("Python only   :", python_only)
print("All skills    :", all_skills)
print("Missing       :", missing)
print("Python covers all required:", required.issubset(python_skills))

candidate = set()
for _ in range(3):
    candidate.add(input("Enter candidate skill: ").strip())

print("\nCandidate skills:", candidate)
print("Matched:", candidate & required)
print("Missing:", required - candidate)
print("Match percentage:", len(candidate & required) / len(required) * 100)
