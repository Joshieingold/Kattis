line_1 = input()
cases, w, h = line_1.split(" ")
cases, w, h = int(cases), int(w), int(h)
box = (w * h)
count = cases
while count > 0:
    match = int(input())
    if match**2 <= w**2 + h**2:
        print("DA")
    else:
        print("NE")
    count -= 1