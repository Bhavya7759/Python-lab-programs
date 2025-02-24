text = input("Enter a string: ")

vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in text.lower():
    if char in vowel_count:
        vowel_count[char] += 1

for vowel, count in vowel_count.items():
    print(f"Frequency of '{vowel}': {count}")
