FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

temperature = float(input("Enter the temperature to convert:"))
temp_type = input("Is this in Celsius or Fahrenheit? (C?F): ").strip().upper()
def convert_to_celsius():
    global temperature
    return (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit():
    global temperature
    return (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
match temp_type:
    case 'C':
        convert_to_fahrenheit()
        print(f"{temperature}°C is {convert_to_fahrenheit()}°F")
    case 'F':
        convert_to_celsius()
        print(f"{temperature}°F is {convert_to_celsius()}°C")
    case _:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")