press = int(input())
initial_num = int(input())
if press % 2 == 1:
    print("still running")
else:
    while press > 1:
        sub_num = int(input())
        initial_num -= sub_num
        if initial_num < 0:
            initial_num = initial_num * -1
        press -= 1
    print(initial_num)
