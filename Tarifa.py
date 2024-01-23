allotted = int(input())
count = int(input())
left_over = 0
while count > 0:
    used = int(input())
    left_over += allotted - used
    count -= 1
print(left_over+allotted)