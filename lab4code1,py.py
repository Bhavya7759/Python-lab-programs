
text = input("Enter a string: ")


print("\nSlicing Demonstrations:")
print(f"Original String: {text}")


print(f"Substring from index 2 to 5: {text[2:6]}")
print(f"Substring from start to index 4: {text[:5]}")


print(f"Substring from index 3 to end: {text[3:]}")


print(f"Last 3 characters: {text[-3:]}")


print(f"Everything except last 2 characters: {text[:-2]}")


print(f"Every second character: {text[::2]}")


print(f"Reversed String: {text[::-1]}")
