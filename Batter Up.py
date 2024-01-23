# first line is num of at-bats
# next line contains x int seperated by spaces
# strike out = 0, singles, doubles, triples, home runs (0-4) walks are -1
# output is all nums divided by the len of the nums
# walks dont count towards output number
num_bats = int(input())
scores = input().split(" ")
total_points = 0
divider = 0
for run in scores:
    run = int(run)
    if run >= 0:
        divider += 1
        total_points += run
print(total_points / divider)