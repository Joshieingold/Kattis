timer = int(input())
goombas = 0
possible = True
while timer > 0:
    this_room_g, minus = map(int, input().split(" "))
    goombas += this_room_g
    if goombas >= minus:
        pass
    elif goombas < minus:
        print("impossible")
        possible = False
        break
    timer -= 1
if possible == True:
    print("possible")