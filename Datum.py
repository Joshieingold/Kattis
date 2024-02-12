# Getting the input
day, month = map(int, input().split(" "))

# Months organized by starting on Sunday - Saturday
february = 2
march = 3
november = 11
june = 6
september = 9
december = 12
april = 4
july = 7
october = 10
january = 1
may = 5
august = 8

# Sundays
if month == february or month == march or month == november:
    lst = [0]
    for i in range(8):
        lst.append("Sunday")
        lst.append("Monday")
        lst.append("Tuesday")
        lst.append("Wednesday")
        lst.append("Thursday")
        lst.append("Friday")
        lst.append("Saturday")
# Mondays
elif month == june:
    lst = [0]
    for i in range(8):
        lst.append("Monday")
        lst.append("Tuesday")
        lst.append("Wednesday")
        lst.append("Thursday")
        lst.append("Friday")
        lst.append("Saturday")
        lst.append("Sunday")
# Tuesdays
elif month == september or month == december:
    lst = [0]
    for i in range(8):
        lst.append("Tuesday")
        lst.append("Wednesday")
        lst.append("Thursday")
        lst.append("Friday")
        lst.append("Saturday")
        lst.append("Sunday")
        lst.append("Monday")
# Wednesdays
elif month == april or month == july:
    lst = [0]
    for i in range(8):
        lst.append("Wednesday")
        lst.append("Thursday")
        lst.append("Friday")
        lst.append("Saturday")
        lst.append("Sunday")
        lst.append("Monday")
        lst.append("Tuesday")
# Thursdays
elif month == october or month == january:
    lst = [0]
    for i in range(8):
        lst.append("Thursday")
        lst.append("Friday")
        lst.append("Saturday")
        lst.append("Sunday")
        lst.append("Monday")
        lst.append("Tuesday")
        lst.append("Wednesday")
# Fridays
elif month == may:
    lst = [0]
    for i in range(8):
        lst.append("Friday")
        lst.append("Saturday")
        lst.append("Sunday")
        lst.append("Monday")
        lst.append("Tuesday")
        lst.append("Wednesday")
        lst.append("Thursday")
# Saturdays
elif month == august:
    lst = [0]
    for i in range(8):
        lst.append("Saturday")
        lst.append("Sunday")
        lst.append("Monday")
        lst.append("Tuesday")
        lst.append("Wednesday")
        lst.append("Thursday")
        lst.append("Friday")
# Prints the day in the lst
print(lst[day])

