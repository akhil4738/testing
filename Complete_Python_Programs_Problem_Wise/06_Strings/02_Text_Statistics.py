"""
CONCEPT: 06 Strings
PROBLEM:
Analyze a paragraph for words, characters, spaces, vowels, consonants and repeated words.

TASK:
1. Read input from the user where appropriate.
2. Validate important input.
3. Perform the required processing.
4. Display a clear formatted report.
5. Test the program with at least three different cases.
"""

print("=" * 70)
print("02 Text Statistics")
print("=" * 70)

text = input("Enter text: ").strip()
normalized = ""
for ch in text.lower():
    if ch.isalnum():
        normalized += ch

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

palindrome = normalized == normalized[::-1]

print("\nTEXT ANALYSIS")
print(f"Original text : {text}")
print(f"Characters    : {len(text)}")
print(f"Words         : {len(text.split())}")
print(f"Vowels        : {vowels}")
print(f"Consonants    : {consonants}")
print(f"Digits        : {digits}")
print(f"Spaces        : {spaces}")
print(f"Palindrome    : {'YES' if palindrome else 'NO'}")
print(f"Uppercase     : {text.upper()}")
print(f"Lowercase     : {text.lower()}")
