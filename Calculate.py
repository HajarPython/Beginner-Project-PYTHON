# Welcome message
print("Welcome to the Simple Calculator!")
print("You can perform operations: +, -, *, /, pow, sqrt.")
print("Type 'exit' to quit the program")

while True:
    # Ask the user for the operation
    operation = input("Enter the operation (+, -, *, /, pow, sqrt) or 'exit' to quit: ").lower()

    # Check if the user wants to exit
    if operation == "exit":
        print("Goodbye!")
        break

    # For operations that need two numbers
    if operation in ["+", "-", "*", "/", "pow"]:
        # Ask for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:  # Prevent division by zero
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        elif operation == "pow":
            result = pow(num1, num2)

        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

    # For the square root operation (only one number needed)
    elif operation == "sqrt":
        num = float(input("Enter the number: "))
        if num >= 0:  # Square root only defined for non-negative numbers
            result = pow(num, 0.5)  # or use math.sqrt(num)
            print(f"The square root of {num} is: {result}")
        else:
            print("Error: Square root of a negative number is not allowed.")

    # If the operation is not recognized
    else:
        print("Invalid operation. Please try again.")