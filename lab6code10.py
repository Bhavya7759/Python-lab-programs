words = ['apple', 'banana', 'cherry', 'kiwi', 'blueberry', 'grape']

n = 5

longer_words = [word for word in words if len(word) > n]

print(f"Words longer than {n}: {longer_words}")
