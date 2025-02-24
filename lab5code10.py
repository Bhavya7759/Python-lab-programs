text = input("Enter a string: ")

if len(text) >= 3:
    if text.endswith('ing'):
        result = text + 'ly'
    else:
        result = text + 'ing'
else:
    result = text

print(f"Result: {result}")
