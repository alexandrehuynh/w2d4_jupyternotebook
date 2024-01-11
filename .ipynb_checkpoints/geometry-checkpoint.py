# 1) Create a Module in VS Code and Import It into jupyter notebook

# Module should have the following capabilities:
from math import pi as p

# 1a) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
def house_sqft(length, width):
    return [length * width]

# 1b) Has a function to calculate the circumference of a circle 2 Pi r
def circumference(radius):
    return [2 *p *radius]