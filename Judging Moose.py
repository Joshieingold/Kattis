x, y = map(int, input().split(" "))
if x == y:
    word = "Even "
elif x != y:
    word = "Odd "
tine = max(x, y) * 2
if tine == 0:
    print("Not a moose ")
else:
    print(word + str(tine))