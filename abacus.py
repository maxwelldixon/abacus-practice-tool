""" This program prints arithmetic problems with numbers ranging from 1-1000
    for practice with an abacus.
"""
from __future__ import division
import random
import time
from datetime import timedelta, date
import re

banner = r'''
       _                                                     _   _                _              _ 
  __ _| |__   __ _  ___ _   _ ___       _ __  _ __ __ _  ___| |_(_) ___ ___      | |_ ___   ___ | |
 / _` | '_ \ / _` |/ __| | | / __|_____| '_ \| '__/ _` |/ __| __| |/ __/ _ \_____| __/ _ \ / _ \| |
| (_| | |_) | (_| | (__| |_| \__ |_____| |_) | | | (_| | (__| |_| | (_|  __|_____| || (_) | (_) | |
 \__,_|_.__/ \__,_|\___|\__,_|___/     | .__/|_|  \__,_|\___|\__|_|\___\___|      \__\___/ \___/|_|
                                       |_|                                                         
'''
list_of_answers = []
start_time = 0
end_time = 0
elapsed_time = ""
date_today = ""

print(banner)
time.sleep(1)

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

        # Asks user for number of problems
        while True: 
                try:
                        num_problems = int(input("How many problems would you like to do? "))
                        if (num_problems < 0 or num_problems > 100):
                            raise ValueError
                except ValueError:
                        print("Please enter another value.")
                        continue
                else:
                        break

        # Starts timer
        print("Starting timer. The timer ends when you enter 'y' to see the answers.")
        start_time = time.time()

        # Loop to create problems 
        for num in range(1, num_problems + 1):
                x = random.randint(1, 1000)
                y = random.randint(1, 1000)

                print(f"{problem_count}. {x} {operator} {y}")
                print("           ")

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

        # Creating a file that records user's progress (ie. completion % and time)
        my_progress = open("abacus_progress.txt", "a")
        
        num_problems = len(list_of_answers)
        date_today = str(date.today())
        time_in_seconds = end_time - start_time 
        elapsed_time = str(timedelta(seconds = time_in_seconds))

        # Checks if value entered by user is type integer
        while True: 
                try:
                        num_correct = int(input("How many problems did you get correct? "))
                        if (num_correct > len(list_of_answers) or num_correct  < 0):
                            print("I don't believe you.") 
                            raise ValueError 
                except ValueError:
                        print("Please enter correct value.")
                        continue
                else:
                        break

        # Writes user's progress to a text file
        my_progress.write(f"On {date_today} you completed {num_problems} problem(s) in {elapsed_time}  Score: {(num_correct / num_problems)*100:.2f}%.\n")

        my_progress.close()

if __name__ == "__main__":
        
        while True:
                binary_operation = input("What type of problems would you like to do? (add for addition, sub for subtraction, mult for multiplication, or div for division): ")
                # Input Validation
                if not re.match(r"^(add|sub|mult|div)$", binary_operation):
                        print("Please enter add, sub, mult, or div.")
                        continue
                else:
                        break

        list_problems(binary_operation)

        ans = input("To view the answers enter 'y': ")

        # If user hits 'y' immediately the timer will display an incorrect time (eg. -18085 days). 
        if ans == "y":
                end_time = time.time()          
                for i in range(0, len(list_of_answers)):                
                        print(f"{str(i+1)}. {str(list_of_answers[i])}")
        else:
                end_time = time.time()  
                print("No answers for you.")

        my_progress_file()
