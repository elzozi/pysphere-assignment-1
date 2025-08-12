# This is a program to calculate the voltage across a wire given the current and resistance
# The formula for volatage is V = IR
# The program will ask the user for the current and resistance and then it will calculate the voltage
# and print it out.
# Author: Elo

current = float(input("Enter the value of the Current (in Amperes): "))
resistance = float(input("Enter the value of the Resistance (in Ohms): "))
voltage = current * resistance
print(f"The voltage of the wire is: {voltage} V ", )  # This line was added to print
