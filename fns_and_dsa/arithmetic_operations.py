#script to perform basic arithmetic operations

def arithmetic_operations(a=0, b=0, operation=None):
    def addition():
        return a + b
    def subtraction():
        return a - b
    def multiplication():
        return a * b
    def division():
        if b != 0:
            return a / b
        else:
            return "Error: Not divisible by zero"
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
 
   