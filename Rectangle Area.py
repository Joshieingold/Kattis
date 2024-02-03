x1, y1, x2, y2 = map(float, input().split(" "))
x = max(x1, x2) - min(x1, x2)
y = max(y1, y2) - min(y1, y2)
print(x * y)