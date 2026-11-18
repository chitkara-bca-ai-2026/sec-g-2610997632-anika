print("=" * 50)
print("             TEXT PROCESSING TOOL")
print("=" * 50)

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

position = int(input("Enter position for indexing: "))

if 0 <= position < len(sentence):
    print("Character at position", position, ":", repr(sentence[position]))
else:
    print("Invalid position")

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))

print("Sliced string [" + str(start) + ":" + str(end) + "] :", repr(sentence[start:end]))

print("Uppercase                   :", sentence.upper())
print("Lowercase                   :", sentence.lower())

old_word = input("Enter word to replace          : ")
new_word = input("Enter replacement word         : ")

print("After replace                 :", sentence.replace(old_word, new_word))
print("Length of sentence            :", len(sentence))

print("\n" + "=" * 50)
print("Analysis Complete!")
print("=" * 50)