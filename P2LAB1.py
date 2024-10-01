import math

"""
Sejiro K.
10/1/42
P2LAB1
Circle Math
"""

print("Welcome to the Circle Calculator! \n")


radius = float(input("What is the radius of your cicle: "))
unit = input("What unit of measurment are you using: ")
pi = math.pi


print()
print()

print("If the radius is", str(radius) + unit, "then: \n\n")


print(f"Diameter = {radius * 2: .2f}{unit}")
print(f"Circumference = {round(2 * pi * radius, 2): .2f}{unit}")
print(f"Area = {round((radius ** 2) * pi, 2): .2f}{unit}^2")


#Note: I tried running this program by clicking it on the desktop, and it closes itself for some reason
