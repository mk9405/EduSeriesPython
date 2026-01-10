# =====================================================
# PYTHON DATETIME
# =====================================================
# Python does not have a built-in date type.
# To work with dates, we use the 'datetime' module.

import datetime

# =====================================================
# CURRENT DATE AND TIME
# =====================================================
# Use datetime.datetime.now() to get the current date and time

x = datetime.datetime.now()
print("Current Date and Time:", x)
# Example Output: 2026-01-11 01:14:44.252185

# Accessing specific parts of the date
print("Year:", x.year)
print("Weekday Name:", x.strftime("%A"))  # %A = full weekday name

# =====================================================
# CREATING DATE OBJECTS
# =====================================================
# Use datetime() constructor: datetime(year, month, day[, hour, minute, second, microsecond, tzinfo])

my_date = datetime.datetime(2020, 5, 17)
print("Created Date:", my_date)

# Including time
my_date_time = datetime.datetime(2020, 5, 17, 15, 30, 45)
print("Created Date and Time:", my_date_time)

# =====================================================
# FORMATTING DATES - strftime()
# =====================================================
# The strftime() method formats date objects into readable strings

my_date = datetime.datetime(2018, 6, 1)
print("Month Name:", my_date.strftime("%B"))  # %B = Full month name (June)

# =====================================================
# COMMON strftime FORMAT CODES
# =====================================================
# Here is a reference table for formatting dates with strftime():

"""
Directive   Description                           Example
%a          Weekday, short version               Wed
%A          Weekday, full version                Wednesday
%w          Weekday as number 0-6, 0=Sunday     3
%d          Day of month 01-31                   31
%b          Month name, short version            Dec
%B          Month name, full version             December
%m          Month as number 01-12                12
%y          Year, short version                  18
%Y          Year, full version                   2018
%H          Hour 00-23                           17
%I          Hour 00-12                           05
%p          AM/PM                                PM
%M          Minute 00-59                         41
%S          Second 00-59                         08
%f          Microsecond 000000-999999            548513
%z          UTC offset                            +0100
%Z          Timezone                               CST
%j          Day number of year 001-366           365
%U          Week number of year, Sunday first   52
%W          Week number of year, Monday first   52
%c          Local version of date and time      Mon Dec 31 17:41:00 2018
%C          Century                               20
%x          Local version of date               12/31/18
%X          Local version of time               17:41:00
%%          A % character                        %
%G          ISO 8601 year                        2018
%u          ISO 8601 weekday (1-7, 1=Monday)    1
%V          ISO 8601 week number (01-53)        01
"""

# Example: Display full date and time
now = datetime.datetime.now()
formatted = now.strftime("%A, %d %B %Y %H:%M:%S")
print("Formatted Date and Time:", formatted)
# Example Output: Sunday, 11 January 2026 01:14:44

# =====================================================
# NOTES:
# 1. datetime module is imported as 'import datetime'
# 2. Use datetime.datetime.now() for current date & time
# 3. Use datetime(year, month, day[, ...]) to create specific dates
# 4. strftime() formats dates into readable strings
# 5. There are many formatting codes for day, month, year, time, timezone
