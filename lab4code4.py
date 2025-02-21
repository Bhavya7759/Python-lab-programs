text = input("Enter a string: ")

def capitalize_first_last(word):
    if len(word) > 1:
        return word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        return word.upper()

words = text.split()

capitalized_words = [capitalize_first_last(word) for word in words]

result = ' '.join(capitalized_words)

print(f"Result: {result}")
