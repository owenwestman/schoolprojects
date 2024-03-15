# Made by Owen Eastman, Jan 29 2024

# get list length and convert to integer, make sure user provides a positive integer
amount = input("How many numbers do you want to average?\n")
# isdigit function checks if the input string is a digit
while not amount.isdigit():
	amount = input("How many *positive integers* do you want to average?\n")
amount = int(amount)
# checks if input is greater than zero
while amount <= 0:
	amount = input("How many *nonzero numbers* do you want to average\n")
	while not amount.isdigit():
		amount = input("How many *positive integers* do you want to average?\n")
	amount = int(amount)

# init other variables
nums = []
tval = 0

# add user's numbers to list and check that they input valid float
for i in range(amount):
	cval = 0
	# try/except to ignore error messages until they stop appearing
	while True:
		try:
			cval = float(input("Number " + str(i+1) + "?\n"))
			break
		except ValueError:
			print("Please enter only numbers (signed float)")
	nums.append(cval)

# add numbers to total value
for j in range(amount):
	tval += float(nums[j])

# divide by amount and return
tval = tval/len(nums)
print(f"The average is: {tval}")
