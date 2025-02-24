text = input("Enter a string: ")

if len(text) < 2:
    result = ""  
else:
    result = text[:2] + text[-2:]

print(f"Result: {result}")
