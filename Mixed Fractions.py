while True:
    divide, by = map(int, input().split(" "))
    if divide == 0 and by == 0:
        break
    whole, remainder = divmod(divide, by)
    print(whole, remainder, "/", by)