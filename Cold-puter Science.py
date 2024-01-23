num = int(input())
x = input()
y = x.split(" ")
count = 0
for number in y:
    if int(number) < 0:
        count += 1
print(count)


#It should be noted that I understand "for" a bit better
# for "every individual item" in list "y" we do this thing.