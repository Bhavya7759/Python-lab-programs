text = input("Enter a string: ")

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character frequencies:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")
