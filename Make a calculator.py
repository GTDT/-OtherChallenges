"""
                By GTDT
              11/19/2020

      Challange: Make a calculator

              4 points

Make a basic and a simple calculator that should contain + - /(division) x(multiplication)
Example: 5x5 = 25    25/5 = 5  5+5 = 10  5-5 = 0
"""


#exec('''def add(y, x): return y + x\ndef subtract(y, x): return y - x\ndef multiply(y, x): return y * x\ndef divide(y, x): return y / x\nN1 = int(input("Enter first number:\\ >> "))\nOperation = input("Select operations from +, -, *, /:\\ >> ")\nN2 = int(input("Enter second number:\\ >> "))\nif Operation == "+": print(N1, "+", N2, "=", add(N1, N2))\nelif Operation == "-": print(N1, "-", N2, "=", subtract(N1, N2))\nelif Operation == "*": print(N1, "*", N2, "=", multiply(N1, N2))\nelif Operation == "/": print(N1, "/", N2, "=", divide(N1, N2))''')
    

def add(y, x):
    return y + x
def subtract(y, x):
    return y - x
def multiply(y, x):
    return y * x
def divide(y, x):
    return y / x
N1 = int(input("Enter first number:\n >> "))
Operation = input("Select operations from +, -, *, /:\n >> ")
N2 = int(input("Enter second number:\n >> "))
if Operation == "+":
    print(N1, "+", N2, "=", add(N1, N2))
elif Operation == "-":
    print(N1, "-", N2, "=", subtract(N1, N2))
elif Operation == "*":
    print(N1, "*", N2, "=", multiply(N1, N2))
elif Operation == "/":
    print(N1, "/", N2, "=", divide(N1, N2))







