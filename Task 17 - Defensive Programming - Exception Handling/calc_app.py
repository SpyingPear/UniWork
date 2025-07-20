x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    if y == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(x / y)
else:
    print("Invalid operation.")