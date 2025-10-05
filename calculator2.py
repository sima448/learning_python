while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    x = input("Choose operation (+, -, *, /) or 'q' to quit: ")

    if x == "q":
        print("Exiting Calculator... Bye!")
        break

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
            print("Invalid operation: Division by zero")
    else:
        print("Invalid operation: Please choose +, -, *, / or q")
