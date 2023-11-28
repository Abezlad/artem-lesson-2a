from math import sqrt

print("_")
print("+")
print("*")
print("/")
print("**")
print("sqr")
print("exit")

x, y = None, None
while True:
    operator = input("Enter one of the operators above: ")

    x = input("Enter first value: ")
    if operator != "sqr":
        y = input("Enter a second value: ")
    else:
        y = "0"

    if (x != None and y != None) and x.isdigit() and y.isdigit():
        x = float(x)
        y = float(y)
    else:
        print("Check x, y values.")
        continue

    if operator == "+":
        t = x + y
        print(f"It is equal: {t}")
    elif operator == "-":
        t = x - y
        print(f"It is equal: {t}")
    elif operator == "*":
        t = x * y
        print(f"It is equal: {t} ")
    elif operator == "/":
        if y == 0:
            print("You can't divide by zero")
        else:
            t = x / y
            print(f"It is equal: {t}")
    elif operator == "**":
        t = pow(x, y)
        print(f"It is equal: {t}")
    elif operator == "sqr":
        t = sqrt(x)
        print(f"It is equal: {t}")
    else:
        print("Error")

    continue_ = input("We continue?(+ / -)")
    if continue_ == "-":
        break