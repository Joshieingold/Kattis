#line 1:
    #n = number of friends
    #k = num of days until birthday
    # The day it is today
# next n lines contains the day they went into quarintine
line_1 = input()
guests, birth, date = line_1.split(" ")
guests, birth, date = int(guests), int(birth), int(date)
accepted = 0
count = guests
while count > 0:
    cur_guest = int(input())
    q_time = date - cur_guest
    if q_time + birth >= 14:
        accepted += 1
    count -= 1
print(accepted)