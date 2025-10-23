# functions.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: 除數不能為 0"
    return a / b

def square(a):
    return a * a