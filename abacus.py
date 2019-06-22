""" This program prints addition problems with numbers ranging from 1-1000
    for practice with an abacus.
"""
import random

# List of answers to addion problems
list_of_answers = []

def addition():

	# Keeps track of how many problems have been assigned
	count = 1
	
	# Asks user how many problems he/she would like to complete
	num_problems = input("How many problems would you like to do? ")
	
	# Loop creating random addition problems that keeps track of their sums
	# and how many problems there are.
	for num in range(1, num_problems + 1):
		x = random.randint(1, 1000)
		y = random.randint(1, 1000)
		print "%d. %d + %d" % (count, x, y)
		print "           "
		sum_xy = x + y
		count += 1
		list_of_answers.append(sum_xy)

def my_progress():

	# Creating a file that records my progress (ie. completion % and time)
	my_progress = open("abacus_progress.txt", "a")
	
	# Number of problems, minutes and seconds taken to complete,
	# number of questions that were incorrect, and date
	num_problems = str(len(list_of_answers))
	date = raw_input("Enter today's date, (eg. 9/14):  ")
	minutes = raw_input("Enter how many minutes it took to complete the problems: ")
	seconds = raw_input("Enter how many seconds it took to complete the problems: ")
	num_wrong = raw_input("Enter how many problems did you get wrong: ")

	# Writes my progress to a text file
	my_progress.write("On " + date + " you completed " + num_problems + " problems in " + minutes + " min " + seconds + " sec, and you missed " + num_wrong + " out of " + num_problems + "." + "\n")
  
	my_progress.close()

if __name__ == "__main__":
	addition()
	ans = raw_input("To view the answers enter Y: ")
	if ans == "Y":
		for i in range(0, len(list_of_answers)):		
			print str(i+1) + ". " + str(list_of_answers[i])
	my_progress()


	 
