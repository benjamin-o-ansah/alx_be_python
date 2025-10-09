'''Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.

'''

class BankAccount:
    
    def __init__(self, accountBalance, initialBalance=0):
        self.accountBalance = accountBalance
        self.initialBalance = initialBalance
    
    def deposit(self,amount):
        self.initialBalance +=amount
        self.accountBalance +=amount
        
    
    def withdraw(self,amount):
        # try:
            
        if self.accountBalance >= amount:
            return True 
                # print(f"Withdrew: ${amount}")
        else:
            return False
        # except Exception as e:
        #     print("Sorry this calculation is out of bounds!")
        # finally:
        #     print("Thank you for choosing to bank with us!")
            
    def display_balance(self):
         print (f"Current Balance: ${self.accountBalance}")