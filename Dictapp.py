import json
import difflib 
from difflib import SequenceMatcher
from difflib import get_close_matches
# see readme for full elaboration 

#the josn file is within the same folder of the py file, so i can write the name directly without pathing
data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return(data[word])
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		results=get_close_matches(word, data.keys())
		results.append('Exit')
		for a, b in enumerate(results, 1):
    			print("{} {}".format(a, b))

		try:
			choice=int(input("Did you mean one of these suggested words? if so, select number, 4 to exit : "))
			if choice != 4:
				return(data[results[choice-1]])
			else:
				return("Exiting Dict app")

		except Exception as e:
			print("failed due to error...", e)
			return("Exiting Dict app")

	else:
		return("Could not find word in Dictionary. Double check it")


print("##### Welcome to Interactive Dictionary App #####\n")
word = input("Please Enter word: ")

output = translate(word)
if type(output) == list:
	for meanings in output:
		print(meanings)	
else:
	print(output)
