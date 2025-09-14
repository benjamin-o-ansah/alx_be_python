#requesting for finanicial details from user

monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# projecting annual savings
# assuming an annual interest rate of 5%

projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")