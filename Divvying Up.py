num_contest = int(input())
prizes = input().split(" ")
total = 0
for prize in prizes:
    total += int(prize)
if total % 3 == 0:
    print("yes")
else:
    print("no")
