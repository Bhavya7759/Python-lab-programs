text = input("Enter a string: ")

words = text.split()

smallest_word = min(words, key=len)

print(f"The smallest word is: {smallest_word}")
