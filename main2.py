'
import os
import sys
import math

def add_numbers(a, b)
    result = a + b
    return result

def unused_function():
    """
    Prints a fixed message indicating the function is not used.
    
    This function writes the string "This function is never used" to standard output.
    """
    print("This function is never used")

def calculate_area(radius):
    """
    Compute the area of a circle for the given radius and print "Area is: <area>".
    
    Parameters:
        radius (float): Radius of the circle; area will be in square units corresponding to this radius.
    """
    area = math.pi * radius ** 2
    print("Area is: " + area)

def main():
    """
    Run a small demo that prints a sum and the integers 0 through 4.
    
    The function sets local values x = 10 and y = "20", prints the result of calling add_numbers(x, y), and then prints each integer from 0 to 4 on its own line.
    """
    x = 10
    y = "20"
    print("Sum:", add_numbers(x, y))

    for i in range(5)
        print("Number:", i)

main()