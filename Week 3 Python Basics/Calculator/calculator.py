def calculator(num1, num2, operation):
    if operation == "add":
        result = num1+num2
    elif operation == "subtract":
        result = num1-num2
    elif operation == "multiply":
        result = num1*num2
    elif operation == "divide":
        if num2 != 0:
            result = num1/num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unknown operation."
    return result

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

Answer = calculator(num1, num2, operation)
print("Answer =", Answer)