import math
x = 0
height, design, velocity, wind_speed = map(int, input().split(" "))
while height > 0:
    velocity += wind_speed
    velocity -= (max(1, math.floor(velocity / 10)))
    if velocity >= design:
        height += 1
    elif 0 < velocity:
          if velocity < design:
            height -= 1
            if height == 0:
                velocity = 0
    elif velocity <= 0:
        height = 0
        velocity = 0
    x += velocity
    if wind_speed > 0:
        wind_speed -= 1

print(round(x))