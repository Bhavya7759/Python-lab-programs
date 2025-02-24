text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

words1 = set(text1.split())
words2 = set(text2.split())

common_words = words1.intersection(words2)

if common_words:
    print(f"Common words: {', '.join(common_words)}")
else:
    print("No common words found.")
