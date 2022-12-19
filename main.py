import time
import os
import platform


def winClear():
    os.system("cls")


if platform.system() == 'Windows':
    winClear()
else:
    os.system("clear")
s = 0
m = 0
h = 0
days = 0
weeks = 0
months = 0
years = 0
decades = 0
centuries = 0
millenniums = 0

while True:
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
        s = 0
    if h == 24:
        days += 1
        h = 0
        m = 0
        s = 0
    if days == 7:
        weeks += 1
        days = 0
        h = 0
        m = 0
        s = 0
    if weeks == 5:
        months += 1
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    if months == 12:
        years += 1
        months = 0
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    if years == 10:
        decades += 1
        years = 0
        months = 0
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    if decades == 10:
        centuries += 1
        decades = 0
        years = 0
        months = 0
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    if centuries == 1000:
        millenniums += 1
        centuries = 0
        decades = 0
        years = 0
        months = 0
        weeks = 0
        days = 0
        h = 0
        m = 0
        s = 0
    print("format: millenniums:centuries:decades:years:months:weeks:days:hours:minutes:seconds:milliseconds")
    print("time: " + str(format(millenniums, '02')) + ":" + str(format(centuries, '02')) + ":" + str(
        format(decades, '02')) + ":" + str(format(years, '02')) + ":" + str(format(months, '02')) + ":" + str(
        format(weeks, '02')) + ":" + str(format(days, '02')) + ":" + str(format(h, '02')) + ":" + str(
        format(m, '02')) + ":" + str(format(s, '02'))
    print("Press 'Control + C' to exit.")
    time.sleep(0.0055)
    if platform.system() == 'Windows':
        winClear()
    else:
        os.system("clear")
    s += 1
