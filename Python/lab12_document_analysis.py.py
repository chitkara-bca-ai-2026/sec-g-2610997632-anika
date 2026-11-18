sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special += 1

total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("\n" + "=" * 50)
print("          DOCUMENT ANALYSIS REPORT")
print("=" * 50)

print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("\n--- Summary ---")
print("Total letters:", total_letters)
print("Vowel percentage:", f"{vowel_percentage:.1f}%")

print("\n" + "=" * 50)
print("Analysis Complete!")
print("=" * 50)