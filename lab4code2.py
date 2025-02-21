
text = input("Enter a string: ")


print("\nBuilt-in String Function Demonstrations:")


print(f"Uppercase: {text.upper()}")


print(f"Lowercase: {text.lower()}")


print(f"Capitalized: {text.capitalize()}")


print(f"Title Case: {text.title()}")


print(f"Swapped Case: {text.swapcase()}")

print(f"Is Alphanumeric? {text.isalnum()}")

print(f"Is Alphabetic? {text.isalpha()}")

print(f"Is Numeric? {text.isdigit()}")

print(f"Is Uppercase? {text.isupper()}")

print(f"Is Lowercase? {text.islower()}")

char = input("Enter a character to check if the string starts with it: ")
print(f"Starts with '{char}'? {text.startswith(char)}")

char = input("Enter a character to check if the string ends with it: ")
print(f"Ends with '{char}'? {text.endswith(char)}")

substring = input("Enter a substring to find: ")
print(f"First occurrence of '{substring}' is at index: {text.find(substring)}")

old_sub = input("Enter the substring to replace: ")
new_sub = input("Enter the new substring: ")
print(f"String after replacement: {text.replace(old_sub, new_sub)}")

print(f"Splitting string into a list: {text.split()}")

words = text.split()
print(f"Joining words with '-': {'-'.join(words)}")

print(f"String after stripping spaces: '{text.strip()}'")

