def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return round(a/b,2) if b != 0 else "Error: cannot divide by zero"

print("10 / 4 =", divide(10, 4))
