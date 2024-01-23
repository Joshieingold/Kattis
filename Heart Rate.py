# n = number of cases that will exist
# b = the number of beats counted
# p = the amount of seconds it has been counted in.
n = int(input())
countdown = n
while countdown > 0:
    line = input()
    b, p = line.split(" ")
    b = float(b)
    p = float(p)
    bps = b / p
    bpm = 60*b / p
    var = 60 / p
    min_bpm = bpm - var
    max_bpm = bpm + var
    print(round(min_bpm, 4), round(bpm, 4), round(max_bpm, 4))
    countdown -= 1
