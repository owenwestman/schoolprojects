# made by Owen Eastman, March 7 2024

# libraries for file manipulation
import os
import os.path
import json

# set to true to enable vote storage
useStorage = False
# check if file exists and has content, makes new file if not
if useStorage:
    if os.path.isfile('votes.json') and os.stat("votes.json").st_size != 0:
        file = open('votes.json')
        data = json.load(file)
    else:
        sampleDict = {
            'georgeVotes': 0,
            'abrahamVotes': 0
        }
        sampleObject = json.dumps(sampleDict, indent=4)
        with open("votes.json", "w") as outfile:
            outfile.write(sampleObject)
        file = open('votes.json')
        data = json.load(file)
# !!! do not modify votes.json in any way !!!

# check user age
while True:
    try:
        voterAge = int(input("How old are you? "))
        if voterAge < 0:
            print("Age must be positive.")
            continue
        else:
            break
    except:
        print("Invalid age. Please input whole number.")
        continue

# allow voter to vote if age is high enough, adds to and shows candidate statistics if useStorage is enabled
if voterAge >= 18:
    while True:
        voterChoice = input("Would you like to vote for (A/B):\nA. George Washington\nB. Abraham Lincoln\n")
        if voterChoice.lower() == "a":
            print("You voted for George Washington.")
            if useStorage:
                data['georgeVotes'] += 1
                print(f"George Washington has {data['georgeVotes']} vote(s)\nAbraham Lincoln has {data['abrahamVotes']} vote(s)")
            break
        elif voterChoice.lower() == "b":
            print("You voted for Abraham Lincoln.")
            if useStorage:
                data['abrahamVotes'] += 1
                print(f"George Washington has {data['georgeVotes']} vote(s)\nAbraham Lincoln has {data['abrahamVotes']} vote(s)")
            break
        else:
            print("Invalid option. Please choose A or B.")
            continue
# still show vote data if user is under 18, but do not allow voting
else:
    print("You are not old enough to vote.")
    if useStorage:
        print(f"George Washington has {data['georgeVotes']} vote(s)\nAbraham Lincoln has {data['abrahamVotes']} vote(s)")

# write voter data to file if useStorage is enabled
if useStorage:
    dataObject = json.dumps(data, indent=4)
    with open("votes.json", "w") as outfile:
        outfile.write(dataObject)