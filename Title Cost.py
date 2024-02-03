title, cap = input().split(" ")
cost = len(title)
cap = float(cap)
if cost > cap:
    print(cap)
else:
    print(cost)