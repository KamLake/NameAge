# This script outputs the user's age based on the birth date entered.
# There are also check in place for if the current date is the user's birthday,
# and if the user has entered a future date, or indicated if they were born today.

import datetime

# Create a variable storing the current date and time.
currentDate = datetime.datetime.now()

# Collect user date of birth as integers, stored in three variables for year, month, and day.
user_year_born = int(input('Enter your 4-digit year of birth:'))
user_month_born = int(input('Enter your 2-digit month of birth:'))
user_day_born = int(input('Enter your 2-digit day of birth:'))

# Creates a variable for storing the users current age
currentAge = (int(currentDate.strftime("%Y")) - user_year_born)

# If the users birthdate matches today's date, this outputs a message and stops the program.
if user_day_born == int(currentDate.strftime("%d")):
    print('Welcome to the world, newborn baby!')
    exit()

# Checks month and day against the current date to determine if user has had a birthday this year.
if user_month_born > int(currentDate.strftime("%m")):
    currentAge -= 1
elif user_month_born == int(currentDate.strftime("%m")):
    if user_day_born > int(currentDate.strftime("%d")):
        currentAge -= 1

# If the user has entered a future date, this outputs a message and stops the program
if currentAge < 0:
    print('You cannot be born in the future!')
    exit()

# Print the current age of the user
print('You are', currentAge, 'years old!')

# This statement only executes if the user indicates that today is their birthday.
if user_month_born == int(currentDate.strftime("%m")) and user_day_born == int(currentDate.strftime("%d")):
        print('Happy birthday!')
