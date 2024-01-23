string = input()
b_count = 0
k_count = 0
for x in string:
    if x == "b":
        b_count += 1
    if x == "k":
        k_count += 1
# Math Part
if b_count == 0 and k_count == 0:
    print("none")
elif b_count == k_count:
    print("boki")
elif b_count > k_count:
    print("boba")
elif b_count < k_count:
    print("kiki")

