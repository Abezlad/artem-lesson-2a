#calculator
from math import sqrt

print("_")
print("+")
print("*")
print("/")
print("**")
print("sqr")
print("exit")

while True:
    operator = input("Enter one of the operators above: ")
    if operator == "+":
        x = float(input("Enter first value: "))
        y = float(input("Enter a second value: "))
        t = x + y
        print(f"It is equal: {t}")
    elif operator == "-":
        x = float(input("Enter first value: "))
        y = float(input("Enter a second value: "))
        t = x - y
        print(f"It is equal: {t}")
    elif operator == "*":
        x = float(input("Enter first value: "))
        y = float(input("Enter a second value: "))
        t = x * y
        print(f"It is equal: {t} ")
    elif operator == "/":
        x = float(input("Enter first value: "))
        y = float(input("Enter a second value: "))
        if y == 0:
            print("You can't divide by zero")
        else:
            t = x / y
            print(f"It is equal: {t}")
    elif operator == "**":
        x = float(input("Enter first value: "))
        y = float(input("Enter power value: "))
        t = pow(x,y)
        print(f"It is equal: {t}")
    elif operator == "sqr":
        x = float(input("Enter value you want to square: "))
        t = sqrt(x)
        print(f"It is equal: {t}")
    else:
        print("Error")

    continue_ = input( "We continue?(+ / -)" )
    if continue_ == "-":
        break