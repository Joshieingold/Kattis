events = int(input())
calendar = set()
while events > 0:
    start, stop = map(int, input().split(" "))
    calendar.update(range(start, stop + 1))
    events -= 1
print(len(calendar))