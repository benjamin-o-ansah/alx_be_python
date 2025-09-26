FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = float(input("Enter the temperature to convert:"))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
def convert_to_celsius(temperature):
    return (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(temperature):
    return (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
match temp_type:
    case 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    case 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    case _:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")