#program to draw a pattern (square) based on user input

pattern_size = int(input("Enter the size of the pattern: "))

while pattern_size <= 0:
    pattern_size = int(input("Please enter a positive integer for the pattern size: "))

i = 0
while i < pattern_size:
    for col in range(pattern_size):
        print("*", end=" ")
    print()  # Move to next line after completing each row
    i += 1