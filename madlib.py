import random

def instructions():
	print("Welcome to this game, the game where you help write the story.\nI will ask you for a type or word, such as noun or verb.")
	print("I will then generate a sentence using your words to see how it is!\n")

noun1 = ""
noun2 = ""
adj1 = ""
adj2 = ""
adj3 = ""

startSent = ["The", "A", "One", "How", "Be", "If", "What", "Who", "When", "Where"]
midSent = ["away from the", "out of the", "in the lake with the", "on the bus", "in the car"]

print("Do you want to play a word game?")
play = input("Enter 'y' or 'n':")
while play == "y":
	instructions()
	noun1 = input("Please type in a noun: ")
	adj1 = input("Now give me an adjective: ")
	verb = input("Now I need a verb: ")
	noun2 = input("Please provide another noun: ")
	adj2 = input("And I need one more adjective: ")
	print(startSent[random.randint(0,len(startSent)-1)], adj2, noun1, verb, midSent[random.randint(0,len(midSent)-1)], adj1, noun2, "!")
	print("Do you want to play again?")
	play = input("Enter 'y' or 'n'")
