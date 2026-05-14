# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "🚫 Can't divide by zero!"

def main():
    print("🧮 Welcome to Alfredo's Calculator 🧮")
    a = float(input("Enter the first number: "))
    op = input("Choose an operation (+, -, *, /): ")
    b = float(input("Enter the second number: "))

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        result = "Unknown operation 🤷‍♂️"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()