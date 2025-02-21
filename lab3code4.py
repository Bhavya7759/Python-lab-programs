a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b:
    print(f"The equal number is: {a}")
elif a == c:
    print(f"The equal number is: {a}")
elif b == c:
    print(f"The equal number is: {b}")
else:
    print("No two numbers are equal.")
