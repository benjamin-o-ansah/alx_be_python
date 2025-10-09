'''
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

robust_division_calculator.py:
Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.

'''

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        result = num / den  # This will automatically raise ZeroDivisionError if den is 0
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except ValueError:
        return "Error: Please enter numeric values only"
    except Exception as e:
        return f"An unexpected error occurred: {e}"