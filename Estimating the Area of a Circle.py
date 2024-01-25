love = False
while love == False:
    radius, marked_points, points_in_circle = map(float, input().split(" "))
    if radius == 0:
        love = True
        break
    pi = 3.141592654
    rs = radius * radius
    estimated_circle = ((points_in_circle * 4 / marked_points)* rs)
    circle = pi * rs
    print(circle, estimated_circle)

