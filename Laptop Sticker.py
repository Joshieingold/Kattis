lw, lh, sw, sh = map(int, input().split())
check = 0
if sh <= lh - 2:
    check += 1
if sw <= lw - 2:
    check += 1
if check < 2:
    print(0)
elif check == 2:
    print(1)