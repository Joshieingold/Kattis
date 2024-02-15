import math
length, radius = map(int, input().split(" "))
square = length * length
circle = math.pi * (radius**2)
good_circle = circle * 0.6366
if square > good_circle:
    print("nope")
elif square <= good_circle:
    print("fits")