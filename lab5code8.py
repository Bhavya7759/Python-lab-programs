text = input("Enter a string: ")

if len(text) > 1:
    first_char = text[0]
    
    modified_text = first_char + text[1:].replace(first_char, '$')
else:
    modified_text = text

print(f"Modified string: {modified_text}")
