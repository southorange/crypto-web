#English paper
#Here is the program in english-python
# define english_paper which takes the arguments words
# words is equal to the raw input (or keystrokes of the user) which displays on the console "Type a word:"
# define a list, called wordlist, which is empty
# for each word in the function english paper (a loop)
# if the length of words (users input) is less then or equal to 0 AND words.isalpha() returns False (isalpha() checks whether or not the string is alphabetic no spaces allowed)
# then return to the console (which starts the if statement over again) "Type something without spaces!"
# Otherwise (elif), if the length of words (users input) is greater then or equal to 1 AND words.isalpha returns True (see description of isalpha())
# Add (append) to the list called wordlist the string of words (users input)
# Otherwise, return to the console (which starts the if statement over again) error

import requests
def english_paper(words):
	words = raw_input('Type a word:')
	wordlist = []
	for words in english_paper:
	    if len(words) <= 0 and words.isalpha() = False:
		return "Type something without spaces!"
	elif len(words) >= 1 and words.isalpha() = True:
	    wordlist.append(words)
	else:
	    return Error
#TODO FIX FORMATTING		
# There would be a multi-line comment here, but alas python doth not contain-th that (eth).
# TODO : Add printing to console all of the users words together
# TODO : Add detection if users words are the same
# TODO : Fix loop
# TODO : Deploy everywhere
# TODO : ???
# TODO : Fork it!



	
