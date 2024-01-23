string = input()
t = string.count("T")
c = string.count("C")
g = string.count("G")
t_points = t * t
c_points = c * c
g_points = g * g
min_count = min(t,c,g)
wonder = min_count * 7
print(t_points + c_points + g_points + wonder)