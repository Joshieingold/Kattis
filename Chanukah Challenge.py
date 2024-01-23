# first line is the num of sets of datat to come
# second is data set name and then the amount of days of hanukah
n = int(input())
count = n
lst = []
while count > 0:
    line = input()
    rank, doh = line.split(" ")
    rank, doh = int(rank), int(doh)
    candles = 0
    lst = range(1, doh + 1, 1)
    for i in lst:
        candles += i + 1
    print(rank, candles)
    count -= 1

