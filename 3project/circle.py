# made by Owen Eastman, Feb 27 2024
import math
pi = math.pi

# get user input and verify that it is valid
while True:
    try:
        dval = float(input("What is the diameter of your circle? "))
        break
    except:
        print("Invalid Float. Please input a number.")

# calculate area and circumference
rval = dval/2
carea = (rval * rval) * pi
ccircum = 2 * pi * rval

# print area and circumference
print(f"The area of your circle is: {carea}")
print(f"The circumfrence of your circle is: {ccircum}")