count = int(input())
room = []
paradox = False
while count > 0:
    action, name = input().split(" ")
    if action == "entry":
        if name in room:
            paradox = True
        else:
            room.append(name)
    elif action == "exit":
        if name not in room:
            paradox = True
        else:
            room.pop(room.index(name))
    if action == "entry":
        action = " entered"
    elif action == "exit":
        action = " exited"
    if paradox == False:
        print(name, action)
    elif paradox == True:
        print(name, action, " (ANOMALY)")
    paradox = False
    count -= 1
