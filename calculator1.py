a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("choose operation: +, -, *, /")
x = input("Enter operation: ")
if x == "+": 
    print("Result:", a + b)
elif x == "-":
    print("Result:", a - b)
elif x == "*":
    print("Result:", a * b)
elif x == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed!")
