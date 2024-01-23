'''
op! = +1
ned = -1
print fucking 7 +-
'''
count = int(input())
volume = 7
while count > 0:
    command = input()
    if command == "Skru op!":
        if volume == 10:
            pass
        else:
            volume += 1
        count -=1
    else:
        if volume == 0:
            pass
        else:
            volume -= 1
        count -= 1
print(volume)