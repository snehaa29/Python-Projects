import json
from difflib import get_close_matches	#To get string matches for suggesting correct words to the user in case he/she makes a typing mistake

data = json.load(open("data.json"))

def meaning(word):
	word = word.lower()		#Ignores any uppercase alphabets since the data set contains all lowercase words
	if word in data:
		return data[word]
	elif word.title() in data:		#Exception is proper nouns like Delhi, Paris that have title case
		return data[word.title()]
	elif word.upper() in data:		#Another exception is abbreviations like USA, NATO that have all uppercase
		return data[word.upper()]	
	suggest = get_close_matches(word, data.keys())	#Gets the 3 closest matches of the wrongly entered word
	if (suggest):
		ans = raw_input("Did you mean " + str(suggest[0]) + "? Type 'Y' or 'N': ").lower() #Suggests only one closest match
		if ans == 'y':
			return data[suggest[0]]		#Returns the word if the user meant to enter the suggested word
		elif ans == 'n':
			return "The word does not exist."		#If not, then sends an error report
		else:
			return "We didn't understand your query."		#If the user enters anything other than a y or n	
	else:
		return "The word does not exist."		#If there are no matches at all, then sends an error report

print "\nThis is an Interactive Dictionary. Search for the words you want to know the meaning of."

quit = 'n'

while (quit != 'y'):
	word = raw_input("\nPlease enter your word: ")
	definitions = meaning(word)
	if type(definitions) == str:
		print definitions
	else:
		for d in definitions:
			print d
	quit = raw_input("\nDo you want to quit? Type 'Y' or 'N': ").lower()
	while (quit != 'y' and quit !='n'):
		quit = raw_input("Do you want to quit? Type 'Y' or 'N': ").lower()

print "\nThank you for using the dictionary! \n"