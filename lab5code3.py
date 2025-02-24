num = 2
count = 0

while count < 4:
    if num % 2 != 0:  
        num += 1
        continue
    print(num)
    count += 1
    num += 1  
