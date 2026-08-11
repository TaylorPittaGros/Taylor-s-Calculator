import math


def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("No real square root for negative numbers")
    return math.sqrt(a)
