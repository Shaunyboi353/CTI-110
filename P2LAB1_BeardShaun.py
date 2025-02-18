# Shaun Beard
# 2/18/2025
# P2LAB1
# making a program solve and display those answers with f-string

import math

radius = float(input("What the raduis of the circle? "))
diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")