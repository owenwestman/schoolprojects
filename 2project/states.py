# Owen Eastman, Feb 8 2024

# init capital variable
capitals = {
    'alabama': 'Montgomery',
    'alaska': 'Juneau',
    'arizona': 'Phoenix',
    'arkansas': 'Little Rock',
    'california': 'Sacramento',
    'colorado': 'Denver',
    'connecticut': 'Hartford',
    'delaware': 'Dover',
    'florida': 'Tallahassee',
    'georgia': 'Atlanta',
    'hawaii': 'Honolulu',
    'idaho': 'Boise',
    'illinois': 'Springfield',
    'indiana': 'Indianapolis',
    'iowa': 'Des Moines',
    'kansas': 'Topeka',
    'kentucky': 'Frankfort',
    'louisiana': 'Baton Rouge',
    'maine': 'Augusta',
    'maryland': 'Annapolis',
    'massachusetts': 'Boston',
    'michigan': 'Lansing',
    'minnesota': 'Saint Paul',
    'mississippi': 'Jackson',
    'missouri': 'Jefferson City',
    'montana': 'Helena',
    'nebraska': 'Lincoln',
    'nevada': 'Carson City',
    'new hampshire': 'Concord',
    'new jersey': 'Trenton',
    'new mexico': 'Santa Fe',
    'new york': 'Albany',
    'north carolina': 'Raleigh',
    'north dakota': 'Bismarck',
    'ohio': 'Columbus',
    'oklahoma': 'Oklahoma City',
    'oregon': 'Salem',
    'pennsylvania': 'Harrisburg',
    'rhode island': 'Providence',
    'south carolina': 'Columbia',
    'south dakota': 'Pierre',
    'tennessee': 'Nashville',
    'texas': 'Austin',
    'utah': 'Salt Lake City',
    'vermont': 'Montpelier',
    'virginia': 'Richmond',
    'washington': 'Olympia',
    'west virginia': 'Charleston',
    'wisconsin': 'Madison',
    'wyoming': 'Cheyenne'
}

#generic error handling that prompts the user again if the input fails
while True:
	ustate = input("Which state would you like the capital of? ").lower()

	try:
		print(ustate.title() + "'s capital is " + capitals[ustate])
		break
	except:
		print("Invalid State")

# remove key from dict
'''
print(capitals)
del capitals['florida']
print(capitals)
'''
