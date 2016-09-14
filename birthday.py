"""
birthday.py
Author: Vinzent
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
name = str(input("Hello, what is your name? "))
month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
if month == "January":
    monthn = 1
if month == "February":
    monthn = 2
if month == "March":
    monthn = 3
if month == "April":
    monthn = 4
if month == "May":
    monthn = 5
if month == "June":
    monthn = 6
if month == "July":
    monthn = 7
if month == "August":
    monthn = 8
if month == "September":
    monthn = 9
if month == "October":
    monthn = 10
if month == "November":
    monthn = 11
if month == "December":
    monthn = 12

year = float(input("And what year were you born in, {0}? ".format(name)))
day = float(input("And the day? "))
if monthn in (12,1,2):
    t = "winterm"
if monthn in (3,4,5):
    t = "springm"
if monthn in (6,7,8):
    t = "summerm"
if monthn in (9,10,11):
    t = "fallm"
if month == "October" and day == 31:
        exc = 1
        print("You were born on Halloween!")
if monthn == todaymonth and day == todaydate:
    print("Happy birthday!")

if t == "winterm":
    mn = "winter baby"
if t == "springm":
    mn = "spring baby"
if t == "summerm":
    mn = "summer baby"
if t == "fallm":
    mn = "fall baby"
    
if year > 2000:
    yt = "two thousands"
if year <= 1999:
    yt = "nineties"
if year <= 1989:
    yt = "eighties"
if year < 1980:
    yt = "Stone age"

print("{0}, you are a {1} of the {2}.".format(name, mn, yt))