num = int(input())
won = 0
while num > 0:
    string = input()
    if "CD" in string:
        pass
    else:
        won += 1
    num -= 1
print(won)