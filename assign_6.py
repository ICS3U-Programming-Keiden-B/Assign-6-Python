#!/usr/bin/env python3
# Created By: Keiden Byrne
# Date: Dec. 14, 2021
# This program tells you the number of days in a month, + extra functions

import time
import constants
from colorama import Fore, Back, Style
import math


# Launched by perform_action() when a user inputs an invalid input
# Displays a list of all possible inputs and asks the user for another input
# launches perform_action() with the given input
def retry():
    print("Invalid input!\n")
    print(constants.FUNC_LIST)
    print("Please enter what you would like to do.")
    action = input(">" + Fore.YELLOW)
    print(Style.RESET_ALL)
    if (action == "Functions") or (action == "functions"):
        print(constants.FUNC_LIST)
        print("Please enter what you would like to do.")
        action = input(">" + Fore.YELLOW)
        print(Style.RESET_ALL)
        perform_action(action)
    else:
        perform_action(action)


# Asks the user if they would like to restart the program
# if 'y', enter_program() is launched again
# 'n' or an invalid input ends the program
def ask_restart():
    print()
    restart = input("Would you like to restart the program?" + Fore.YELLOW +
                    " y/n" + Style.RESET_ALL + "\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)
    time.sleep(1)
    if (restart == "y") or (restart == "Y"):
        enter_program()
    elif (restart == "n") or (restart == "N"):
        print("Have a good day!")
    else:
        print("Invalid input.")
        print("Have a good day!")


# The problem I chose for assignment 6
def enter_words():
    print("Booting"+Fore.YELLOW+" Words "+Style.RESET_ALL+"program.\n")
    time.sleep(1)

    print("Hi! Enter a sentence and this program will return back all words"
          " located at odd positions.")
    sentence = input(">" + Fore.YELLOW)
    print(Style.RESET_ALL)

    sentence_list = []
    odd_list = []
    sentence_list = sentence.split()

    for counter in range(0, len(sentence_list)):
        if ((counter % 2) == 0):
            odd_list.append(sentence_list[counter])

    print("The words at odd positions are: " + Fore.YELLOW, end="")

    for num in range(0, len(odd_list)):
        if (num != (len(odd_list) - 1)):
            print(odd_list[num], end=", ")
        else:
            if (len(odd_list) != 1):
                print("and", odd_list[num])
            else:
                print(odd_list[num])
    print(Style.RESET_ALL, end="")

    ask_restart()


# Calculates the surface area of a square pyramid
def find_surf_area(height, base):
    area_of_base = base * base
    surf_area = (area_of_base + 2 * base *
                 math.sqrt(area_of_base / 4 + height ** 2))

    sa_half_rounded = int(surf_area * 10 + 0.5)
    surf_area_final = float(sa_half_rounded) / 10

    return surf_area_final


# Calculates the volume of a square pyramid
def find_volume(height, base):
    area_of_base = base * base
    volume = area_of_base * (height / 3)

    vol_half_rounded = int(volume * 10 + 0.5)
    volume_final = float(vol_half_rounded) / 10

    return volume_final


# Takes the height and base of a pyramid as input
# Takes units for the pyramid as input
# Catches invalid heights, bases, and units
# After displaying the SA and Volume, launches ask_restart()
def calc_pyramid():
    print("Booting"+Fore.YELLOW+" Pyramid "+Style.RESET_ALL+"program.\n")
    time.sleep(1)

    print("Hello! This program can calculate the surface area and volume"
          " of a square pyramid.")
    usr_height = input("Please insert a height for the pyramid:\n>"
                       + Fore.YELLOW)
    print(Style.RESET_ALL)

    usr_base = input("Please insert the length of the base:\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)

    units = input("In what units would you like your pyramid?"
                  " (cm/km/m/ft/yrds/in)\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)

    possible_units = ["CM", "KM", "M", "FT", "YRDS", "IN"]
    invalid_text = "Invalid input!"
    invalid = False

    try:
        usr_height_int = int(usr_height)
        usr_base_int = int(usr_base)

    except Exception:
        print(invalid_text, "(Inserted string/float instead of int)",
              end="")
        invalid = True
        invalid_text = ""

    try:
        units = units.upper()
        possible_units.index(units)

    except Exception:
        print(invalid_text, "(Inserted invalid unit measurement type)",
              end="")
        invalid = True
        invalid_text = ""

    if invalid is False:
        usr_surf_area = find_surf_area(usr_height_int, usr_base_int)
        usr_volume = find_volume(usr_height_int, usr_base_int)

        print("Your pyramid's surface area is", str(usr_surf_area),
              units.lower() + "^2.")
        print("Your pyramid's volume is", str(usr_volume), units.lower()
              + ".")
    else:
        print()

    ask_restart()


# Takes the year, month, and day as input to show how many days have passed
# Since last year, and how many days until next year.
# Invalid year and day inputs are caught and prevent the rest of the program
# from running.
# Day inputs under 0 or over the size of the inputted month are caught and
# Display 'Invalid day input.'
# Invalid months are caught and display 'Invalid month input.'
# After displaying the info, the program launches ask_restart()
def enter_days():
    print("Booting" + Fore.YELLOW + " Days " + Style.RESET_ALL + "program.\n")
    time.sleep(1)

    print("Welcome. Enter today's date, and this program will display "
          "how many days have passed since last year, and how many more"
          " days until next year.")
    year = input("What year is it?\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)
    month = input("What month is it?\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)
    day = input("What day of the month is it?\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)

    invalid = False

    try:
        year = int(year)
    except year:
        print("Invalid year input.")
        invalid = True
    try:
        day = int(day)
    except day:
        print("invalid day input.")
        invalid = True

    if invalid is False:
        leap = year % 4
        if (leap == 0):
            leap = 1
        else:
            leap = 0

        if (month == "January") or (month == "january"):
            if (day > constants.JANUARY) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.JANUARY_YEAR + day
        elif (month == "February") or (month == "february"):
            if (day > (constants.FEBRUARY + leap)) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.FEBRUARY_YEAR + day
        elif (month == "March") or (month == "march"):
            if (day > constants.MARCH) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.MARCH_YEAR + day + leap
        elif (month == "April") or (month == "april"):
            if (day > constants.APRIL) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.APRIL_YEAR + day + leap
        elif (month == "May") or (month == "may"):
            if (day > constants.MAY) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.MAY_YEAR + day + leap
        elif (month == "June") or (month == "june"):
            if (day > constants.JUNE) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.JUNE_YEAR + day + leap
        elif (month == "July") or (month == "july"):
            if (day > constants.JULY) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.JULY_YEAR + day + leap
        elif (month == "August") or (month == "august"):
            if (day > constants.AUGUST) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.AUGUST_YEAR + day + leap
        elif (month == "September") or (month == "september"):
            if (day > constants.SEPTEMBER) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.SEPTEMBER_YEAR + day + leap
        elif (month == "October") or (month == "october"):
            if (day > constants.OCTOBER) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.OCTOBER_YEAR + day + leap
        elif (month == "November") or (month == "november"):
            if (day > constants.NOVEMBER) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.NOVEMBER_YEAR + day + leap
        elif (month == "December") or (month == "december"):
            if (day > constants.DECEMBER) or (day <= 0):
                print("Invalid day input.")
                invalid = True
            else:
                day_count = constants.DECEMBER_YEAR + day + leap
        else:
            print("Invalid month input.")
            invalid = True

        if invalid is False:
            print(Fore.YELLOW + str(day_count) + Style.RESET_ALL + " days have"
                  " passed since the beginning of the year. " + Fore.YELLOW +
                  str(365 + leap - day_count) + Style.RESET_ALL + " day(s)"
                  " until the end!")

    ask_restart()


# Shows how many days are in a week
# After displaying the info, the program launches ask_restart()
def enter_weeks():
    print("Booting" + Fore.YELLOW + " Weeks " + Style.RESET_ALL + "program.\n")
    time.sleep(1)

    print("Welcome. This program shows how many days are in a week.\n")
    print("There are" + Fore.YELLOW + " 7 " + Style.RESET_ALL + "days in a"
          " week!")
    ask_restart()


# Displays how many days are in a month based on the user's input
# An invalid input displays 'Invalid input.'
def find_month(value):
    cases = {
        'January': lambda: print("January has " + Fore.YELLOW + "31"
                                 + Style.RESET_ALL + " days."),
        'February': lambda: print("February has "+Fore.YELLOW+"28"
                                  + Style.RESET_ALL + " days, or " +
                                  Fore.YELLOW + "29" + Style.RESET_ALL +
                                  " during a leap year."),
        'March': lambda: print("March has " + Fore.YELLOW + "31"
                               + Style.RESET_ALL + " days."),
        'April': lambda: print("April has " + Fore.YELLOW + "30"
                               + Style.RESET_ALL + " days."),
        'May': lambda: print("May has " + Fore.YELLOW + "31"
                             + Style.RESET_ALL + " days."),
        'June': lambda: print("June has " + Fore.YELLOW + "30"
                              + Style.RESET_ALL + " days."),
        'July': lambda: print("July has " + Fore.YELLOW + "31"
                              + Style.RESET_ALL + " days."),
        'August': lambda: print("August has " + Fore.YELLOW + "31"
                                + Style.RESET_ALL + " days."),
        'September': lambda: print("September has " + Fore.YELLOW + "30"
                                   + Style.RESET_ALL + " days."),
        'October': lambda: print("October has " + Fore.YELLOW + "31"
                                 + Style.RESET_ALL + " days."),
        'November': lambda: print("November has " + Fore.YELLOW + "30"
                                  + Style.RESET_ALL + " days."),
        'December': lambda: print("December has " + Fore.YELLOW + "31"
                                  + Style.RESET_ALL + " days."),
        'january': lambda: print("January has " + Fore.YELLOW + "31"
                                 + Style.RESET_ALL + " days."),
        'february': lambda: print("February has "+Fore.YELLOW+"28 "
                                  + Style.RESET_ALL + "days, or " + Fore.YELLOW
                                  + "29" + Style.RESET_ALL + " during a leap"
                                  " year."),
        'march': lambda: print("March has " + Fore.YELLOW + "31"
                               + Style.RESET_ALL + " days."),
        'april': lambda: print("April has " + Fore.YELLOW + "30"
                               + Style.RESET_ALL + " days."),
        'may': lambda: print("May has " + Fore.YELLOW + "31"
                             + Style.RESET_ALL + " days."),
        'june': lambda: print("June has " + Fore.YELLOW + "30"
                              + Style.RESET_ALL + " days."),
        'july': lambda: print("July has " + Fore.YELLOW + "31"
                              + Style.RESET_ALL + " days."),
        'august': lambda: print("August has " + Fore.YELLOW + "31"
                                + Style.RESET_ALL + " days."),
        'september': lambda: print("September has " + Fore.YELLOW + "30"
                                   + Style.RESET_ALL + " days."),
        'october': lambda: print("October has " + Fore.YELLOW + "31"
                                 + Style.RESET_ALL + " days."),
        'november': lambda: print("November has " + Fore.YELLOW + "30"
                                  + Style.RESET_ALL + " days."),
        'december': lambda: print("December has " + Fore.YELLOW + "31"
                                  + Style.RESET_ALL + " days.")
    }
    cases.get(value, lambda: print("Invalid input."))()


# The user enters a month and the program displays how many days are in that
# Month through find_month()
# An invalid input displays 'Invalid input.'
# After displaying the info, the program launches ask_restart()
def enter_months():
    print("Booting" + Fore.YELLOW + " Months " + Style.RESET_ALL +
          "program.\n")
    time.sleep(1)

    print("Welcome. Enter a month, and this program will display how many days"
          " are in that month.")
    month = input("Please input a month.\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)
    find_month(month)

    ask_restart()


# Displays how many days (normal + leap year), weeks, months, and years are in
# A year
# After displaying the info, the program launches ask_restart()
def enter_years():
    print("Booting"+Fore.YELLOW+" Years "+Style.RESET_ALL+"program.\n")
    time.sleep(1)

    print("Welcome. This program shows how many days, weeks, and months are "
          "in a year.\n")
    print("There are"+Fore.YELLOW+" 365 "+Style.RESET_ALL+"days in a year, or"
          + Fore.YELLOW + " 366 " + Style.RESET_ALL + "days in a leap year," +
          Fore.YELLOW + " 52 " + Style.RESET_ALL + "weeks in a year, and" +
          Fore.YELLOW + " 12 " + Style.RESET_ALL + "months in a year.")

    ask_restart()


# Launches enter_days() if 'days' is inputted
# Launches enter_weeks() if 'weeks' is inputted
# Launches enter_months() if 'months' is inputted
# Launches enter_years() if 'years' is inputted
# If there is an invalid input, retry() is launched
def perform_action(value):
    cases = {
        'days': lambda: enter_days(),
        'Days': lambda: enter_days(),
        'weeks': lambda: enter_weeks(),
        'Weeks': lambda: enter_weeks(),
        'months': lambda: enter_months(),
        'Months': lambda: enter_months(),
        'years': lambda: enter_years(),
        'Years': lambda: enter_years(),
        'pyramid': lambda: calc_pyramid(),
        'Pyramid': lambda: calc_pyramid(),
        'words': lambda: enter_words(),
        'Words': lambda: enter_words()

    }
    cases.get(value, lambda: retry())()


# A small interface before the actual calculating begins
# Perform_action() is launched with the user's input
# If the user inputs 'functions', a list is diplayed and they can enter another
# Input before starting perform_action()
def enter_program():
    print("Please enter what you would like to do, or type" + Fore.YELLOW +
          " functions " + Style.RESET_ALL + "to view all possible inputs.")
    action = input(">"+Fore.YELLOW)
    print(Style.RESET_ALL)
    if (action == "Functions") or (action == "functions"):
        print(constants.FUNC_LIST)
        print("Please enter what you would like to do.")
        action = input(">"+Fore.YELLOW)
        print(Style.RESET_ALL)
        perform_action(action)
    else:
        perform_action(action)


# User enters into the program, and are given the option to either activate the
# Rest of the program or not.
# An invalid input is taken as a 'no' and ends the program
# Entering 'y' starts enter_program()
def main():
    print("Hi! This program can tell you how many days in a month, year, etc.")
    start = input("Would you like to start the program?" + Fore.YELLOW +
                  " y/n" + Style.RESET_ALL + "\n>" + Fore.YELLOW)
    print(Style.RESET_ALL)
    time.sleep(1)

    if (start == "y") or (start == "Y"):
        print("Thank you for using our services today!")
        enter_program()
    elif (start == "n") or (start == "N"):
        print("Have a good day!")
    else:
        print("Invalid input.")
        print("Have a good day!")


if __name__ == "__main__":
    main()
