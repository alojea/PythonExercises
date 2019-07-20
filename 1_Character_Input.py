# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# 1. Add on to the previous program by asking the user for another number and
#     printing out that many copies of the previous message.
#     (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
#     (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import timedelta
from datetime import date

name = input("Insert your name \n")

while True:
    try:
        age = int(input("Insert your age \n"))
        if age > 100:
            print("Value need to be < 100")
        else:
            break
    except ValueError:
        print("Error! Insert a correct value")

future_age = 100 - age

print("You have " + str(age) + " and you will have 100 year old in " + str(date.today() + timedelta(days=(future_age * 365))))
