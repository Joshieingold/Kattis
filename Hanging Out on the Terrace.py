limit, count = map(int, input().split(" "))
people = 0
not_entered = 0
while count > 0:
    word, num = input().split(" ")
    num = int(num)
    if word == "enter":
        if people + num > limit:
            not_entered += 1
        else:
            people += num
    elif word == "leave":
        people -= num
    count -= 1
print(not_entered)