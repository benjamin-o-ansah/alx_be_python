num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /) "))
match operation:
    case "+":
            print(f"The result is {num1 + num2}.")
    case "-":
            print(f"The result is {num1 - num2}.")
    case "*":
            print(f"The result is {num1 * num2}.")
    case "/":
        if (num1 ==0 or num2 ==0):
            print("Division by zero is not allowed.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("Invalid operation selected.")