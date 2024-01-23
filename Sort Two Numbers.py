line = input()
a, b = line.split(" ")
a, b = int(a), int(b)
if a > b:
    print(b, a)
elif b > a:
    print(a, b)
else:
    print(a, b)