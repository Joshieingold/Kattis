from math import ceil,sin,radians
# h = the height of the wall, v = angle of ladder
#output is the min height of ladder
line_1 = input()
height, angle = line_1.split(" ")
height, angle = int(height), int(angle)

print(ceil(height / sin(radians(angle))))