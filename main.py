import time
import os
import datetime
import termcolor

os.system("clear")
s = 50
m = 59
h = 23
days = 6
weeks = 4
months = 0
years = 0
decades = 0
centuries = 0
millenium = 0

while True:
    if (s == 60):
        m += 1
        s = 0
    if (m == 60):
        h += 1
        m = 0
        s = 0
    if (h == 24):
        days += 1
        h = 0
        m = 0
        s = 0
    if (days == 7):
        weeks += 1
        days = 0
        h = 0
        m = 0
        s = 0
    if (datetime.datetime.now().month == 2):
        print("it's February!")
    if (weeks == 5):
        months += 1
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    print("format: millenium:centuries:decades:years:months:weeks:days:hours:minutes:seconds")
    print("time: " + str(format(millenium, '02')) + ":" + str(format(centuries, '02')) + ":" + str(format(decades, '02')) + ":" + str(format(years, '02')) + ":" + str(format(months, '02')) + ":" + str(format(weeks, '02')) + ":" + str(format(days, '02')) + ":" + str(format(h, '02')) + ":" + str(format(m, '02')) + ":" + str(format(s, '02')))
    print("Press 'Control + C' to exit.")
    time.sleep(1)
    os.system("clear")
    s += 1
