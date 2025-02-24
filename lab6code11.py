def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = have_common_member(list1, list2)

print("Do the lists have at least one common member?", result)
