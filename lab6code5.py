sample_list = ['abc', 'xyz', 'aba', '1221']

count = 0

for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]: 
        count += 1

print(f"Number of strings where the first and last character are the same: {count}")
