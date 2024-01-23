cells = int(input())
lanes = int(input())
counter = lanes
total = 0
while counter > 0:
    string = input()
    periods = string.count(".")
    total = total + periods
    counter -= 1
spaces = cells * lanes
if total == 0:
    print(0)
else:
    x = spaces / total
    print(1 / x)