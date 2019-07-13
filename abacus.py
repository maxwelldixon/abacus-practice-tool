""" This program prints arithmetic problems with numbers ranging from 1-1000
    for practice with an abacus.
"""
from __future__ import division
import random
import time
from datetime import timedelta, date

list_of_answers = []
start_time = 0
end_time = 0
elapsed_time = ""
date_today = ""

def list_problems(binary_operation):

	global start_time

	if binary_operation == "add":
		operator = "+"
	elif binary_operation == "sub":
		operator = "-"
	elif binary_operation == "mult":
		operator = "*"
	elif binary_operation == "div":
		operator = "/"

	# Keeps track of how many problems have been assigned
	problem_count = 1

	# Asks user how many problems he/she would like to complete
	num_problems = input("How many problems would you like to do? ")
	
	# Starts timer
	print "Starting timer. The timer ends when you enter 'y' to see the answers."
	start_time = time.time()

	# Loop to create problems 
	for num in range(1, num_problems + 1):
		x = random.randint(1, 1000)
		y = random.randint(1, 1000)

		print "%d. %d %s %d" % (problem_count, x, operator, y)
		print "           "

		output = calculation(binary_operation, x, y)

		problem_count += 1

		list_of_answers.append(output)

def calculation(binary_operation, x, y):
	
	if binary_operation == "add":
		return x + y
	elif binary_operation == "sub":
		return x - y
	elif binary_operation == "mult":
		return x * y
	elif binary_operation == "div":
		return x / y

def my_progress_file():
	
	global elapsed_time	
	global date_today

	# Creating a file that records my progress (ie. completion % and time)
	my_progress = open("abacus_progress.txt", "a")
	
	# Number of problems, today's date,  minutes and seconds taken to complete,
	# number of questions that were incorrect
	num_problems = str(len(list_of_answers))
	date_today = str(date.today())
	time_in_seconds = end_time - start_time 
	elapsed_time = str(timedelta(seconds = time_in_seconds))
	num_wrong = raw_input("How many problems did you get wrong? ")

	# Writes my progress to a text file
	my_progress.write("On " + date_today + " you completed " + num_problems + " problem(s) in " + elapsed_time + " and you missed " + num_wrong + " out of " + num_problems + "." + "\n")
  
	my_progress.close()

if __name__ == "__main__":
	
	binary_operation = raw_input("What type of problems would you like to do? Enter add for addition, sub for subtraction, mult for multiplication, or div for division: ")
	
	list_problems(binary_operation)

	ans = raw_input("To view the answers enter 'y': ")
	
	# If user hits 'y' immediately the timer will display an incorrect time (eg. -18085 days). 
	if ans == "y":
		end_time = time.time()		
		for i in range(0, len(list_of_answers)):		
			print str(i+1) + ". " + str(list_of_answers[i])

	my_progress_file()


	 
