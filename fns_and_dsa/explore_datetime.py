#script to tell the current date and time and also tell a future date and time after adding some days

from datetime import datetime, timedelta
# Get the current date and time
now = datetime.now()
def display_current_datetime(): 
    current_date = now
    print(f"Current date and time: {current_date.date()} {current_date.hour}:{current_date.minute}:{current_date.second}")


def calculate_future_date(days_to_add):
    # Get user input for number of days to add
    
    
    # Calculate future date
    future_date = now + timedelta(days=days_to_add)
    
    return future_date
display_current_datetime()
days_to_add = int(input("Enter the number of days to add to the current date: "))
future_date = calculate_future_date(days_to_add)
print(f"Future date:", future_date.date())