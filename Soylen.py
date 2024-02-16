count = int(input())
while count > 0:
    num = int(input())
    if num % 400 == 0:
        print(num // 400)
    else:
        print((num // 400) + 1)
    count -= 1