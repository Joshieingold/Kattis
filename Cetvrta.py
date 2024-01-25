all_for_one = []
x = []
y = []
count = 3
while count > 0:
    data = input()
    (all_for_one).append(data.split(" "))
    count -= 1
x.append(all_for_one[0][0])
x.append(all_for_one[1][0])
x.append(all_for_one[2][0])
y.append(all_for_one[0][1])
y.append(all_for_one[1][1])
y.append(all_for_one[2][1])
for i in x:
    if x.count(i) == 1:
        x_miss = i
for i in y:
    if y.count(i) == 1:
        y_miss = i
print(x_miss, y_miss)