#script to perform basic arithmetic operations

def perform_operation(num1, num2, operation=None):
    def addition():
        return num1 + num2
    def subtraction():
        return num1 - num2
    def multiplication():
        return num1 * num2
    def division():
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Not divisible byy zero"
    match operation:
        case "add":
            return addition()
        case "subtract":
            return subtraction()
        case "multiply":
            return multiplication()
        case "divide":
            return division()
        case _:
            return "Error: Invalid operation"
 
   