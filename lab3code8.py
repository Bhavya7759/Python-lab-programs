
num = int(input("Enter a number: "))


if num % 2 == 0:
    result = num ** 2  
    print(f"The number is even. Square of {num} is: {result}")
else:
    result = num ** 3 
    print(f"The number is odd. Cube of {num} is: {result}")
