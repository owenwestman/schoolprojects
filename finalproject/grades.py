# made by Owen Eastman, March 27 2024

import random
# random number library

# random number 0 ≤ i ≤ 100
grade = random.randint(0,100)

# blank string, to be assigned later
letterGrade = "";

# a vs an, it would probably be fine with just a or an but it is annoying to me
aan = "a"

# cony grade scale, aan switches for A and F
if grade >= 93:
	letterGrade = "A"
	aan = "an"
elif grade >= 85:
	letterGrade = "B"
elif grade >= 76:
	letterGrade = "C"
elif grade >= 70:
	letterGrade = "D"
else:
	letterGrade = "F"
	aan = "an"

# print results
print(f"Your grade is {aan} {letterGrade} of {grade}!")

# if grade is F, tell user to get better
if letterGrade == "F":
	print("You should pay more attention probably.")
