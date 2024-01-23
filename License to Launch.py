license = int(input())
count = 0
days = list(map(int, input().split(" ")))
minimum = 100000000000
for i in days:
    if i < minimum:
        minimum = int(i)
#print(minimum)
for i in days:
    if i == minimum:
        print(count)
        break
    else:
        count += 1