#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Prince Dungrani"
The python code in this file (a1_[120669221].py) is original work written by
"Prince Dungrani". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

# importing functions and libraries.

import sys
from datetime import datetime

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...
    if month == 2:  # February
        return 29 if leap_year(year) else 28
    if month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = 1  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...
    print("Usage: python3 assignment1.py <startdate> <enddate>")
    sys.exit(1)
    
def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    ...
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...
    print(f"Validating date: {date}")
    try:
        datetime.strptime(date, "%Y-%m-%d")

        year, month, day = map(int, date.split('-'))
        
        if len(str(year)) != 4:  # year must be 4 digits or else will return false
            return False
        
        if month < 1 or month > 12: # month must be >1 or < 12
            return False
        
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    
    except ValueError:
        return False  

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...
    count = 0
    current_date = start_date

    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))

        day_of_week_result = day_of_week(year, month, day)

        
        
        if day_of_week_result == 'sat' or day_of_week_result == 'sun':
            count += 1

        current_date = after(current_date)


    return count

# to compare date in main function, if user enters date incorrectly, it will swap the dates.

def dates_compare(start: str, end: str) -> tuple:
    ''' corrects the date formet'''
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    
    if start_date > end_date:
        return end, start
    return start, end
    


def main_block():
    '''this functions is created because i can use the variables from above functions and is a good practice for object-oriented programming. 
    later on, i will call this function in main function'''
    # checking if user has entered argumnets correctly
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    # calling valid_dates function ot check the dates
    if not valid_date(start_date) or not valid_date(end_date):
        print("Invalid date format. Please ensure both dates are in the format YYYY-MM-DD.")
        usage()

    # swaping dates 
    start_date, end_date = dates_compare(start_date, end_date)

    # calling day_count function to calculate function.
    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days")


if __name__ == "__main__":
    ...
    #calling main block function.
    main_block()
 
   