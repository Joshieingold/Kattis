n,h,v = input().split(" ")
n = int(n)
h = int(h)
v = int(v)
top_left = (h*v)
a = n - v
bottom_left = h * a
b = n - h
top_right = v * b
c = n - h
d = n - v
bottom_right = c * d
tlv = top_left * 4
blv = bottom_left * 4
trv = top_right * 4
brv = bottom_right * 4
print(max(tlv,blv,trv,brv))