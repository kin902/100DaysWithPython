# Exercise 24 day_010
"""
Function with output
def func name(input):
    do something with input
    then do this with input
    final return output
name = func name(input)
print(name)

input
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year_input, month_input):
    """ Put in a year and month and it will return the days in that year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_input == 2:
        if is_leap(year_input):
            return 28 + 1
        elif not is_leap(year_input):
            return 28
    else:
        return month_days[month_input - 1]


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)