    
sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
answers1 = ["function","args","undefined","boolean"]

sample2 = '''___1___ will end the smallest loop it is in and control flows to the statement immediately below the loop.
___2___ causes to end the current iteration of the loop, but not the whole loop. ___3___ is used to define a new user-defined class in Python. 
___4___ is used with try.except block to close up resources or file streams.'''

answers2 = ["break","continue","class","finally"]

sample3 = '''A ___1___   is a way to store data just like a list. 
___2___ has the advantage of providing one ordinal for every character in every script used in modern and ancient texts
the python ___3___ is usually installed as /usr/local/bin/python Python is an ___4___  language. '''

answers3 = ["dictionary","unicode","interpreter","interpreted"]


difficulties = ['easy','medium','hard']
selected_difficulty = raw_input('select easy, medium, or hard: ').lower()

maxReplacement=3
maxTries=0
alreadytyped = []



def game(test, answers):
	"""
	function with two arguments, test to select which sample will be printed, and answers, to select which answer key is used. 
	The function uses a while loop to print the selected test, and prompt a type input until either wrong guesses have been exceeded, or 
	the count variable is the same lenth as the answe key. 
	"""
	count = 0

	while True:
		print test

		typed = raw_input()

		if typed == answers[count] and answers[count] not in alreadytyped:
			alreadytyped.append(answers[count])
			# adds answer to alreadytyped list. 

			test = test.replace('___' + str(count + 1) + '___', answers[count], maxReplacement)

			# replace first 3 instances of ___#___ with answer in list
			count += 1 
 
			print "correct!"
		if count == len(answers):
			print test
			print 'winner'
			break
		if typed not in answers:
			print 'wrong bozo'

			

		




if selected_difficulty == difficulties[0]:
	game(sample1, answers1)
if selected_difficulty == difficulties[1]:
	game(sample2, answers2)
if selected_difficulty == difficulties[2]:
	game(sample3, answers3)
