# made by Owen Eastman, Feb 27 2024

# function to check input
def getin(stype):
    while True:
        try:
            result = float(input(f"What is the {stype} of your rectangle? "))
            break
        except:
            print("Invalid Float. Please input a number.")
    return result

# run function to get user inputs
rectl = getin("length")
rectw = getin("width")

# print output
print(f"The perimeter of your rectangle is: {2*(rectl + rectw)}")