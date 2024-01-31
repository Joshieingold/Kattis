num_lecture = int(input())
check = input()
awake = 0
count = 0
for i in check:
    if i == "1":
        awake = 3
    elif i == "0":
        awake -= 1
    if awake > 0:
        count += 1
print(count)