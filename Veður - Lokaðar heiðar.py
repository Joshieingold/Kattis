v = int(input())
n = int(input())
count = n
while count > 0:
    s = input()
    a, b = s.split(" ")
    b = int(b)
    if v <= b:
        print(a + " opin")
    elif v > b:
        print(a + " lokud")
    else:
        print("error")
    count -= 1
