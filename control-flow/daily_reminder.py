#Python script to ask the user for a single task, it's priority level and if it is time sensitive
task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_sensitive = str(input("Is it time-bound? (yes/no): ")).lower()
match priority:
    case "high":
        if time_sensitive == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_sensitive == "yes":
            print(f"Reminder: '{task}' is is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_sensitive == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")