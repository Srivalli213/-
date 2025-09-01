# Simple Calculator in Python

# Functions for operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main program
print("Simple Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Taking user input
choice = input("Enter choice (1/2/3/4): ")

# Convert inputs to float (for decimals too)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check choice and perform operation
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")


