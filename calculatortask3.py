import math

op = input("enter op(+, /, *, -, sin, cos, tan, cot, factorial, sqrt):")

if op == "/":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    if b == 0:
        r = "Error"
    else:
        r = a / b

if op == "*":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a * b

if op == "+":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a + b

if op == "-":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a - b

if op == "cos":
    a = float(input("Enter a:"))
    r = (math.cos(math.radians(a)))

if op == "cot":
    a = float(input("Enter a:"))
    r = 1/(math.tan(math.radians(a)))

if op == "sin":
    a = float(input("Enter a:"))
    r = (math.sin(math.radians(a)))

if op == "sqrt":
    if a<0:
        r=("error")
    else:
     r = (math.sqrt(a))

if op == "tan":
    a = float(input("Enter a:"))
    r = (math.tan(math.radians(a)))

if op == "factorial":
    a = int(input("Enter a:"))
    r = (math.factorial(a))

print(r)