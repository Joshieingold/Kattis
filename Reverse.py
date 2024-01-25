count = int(input())
lst = []
s_count = count
while count > 0:
    lst.append(input())
    count -=1
while s_count > 0:
    print(lst[-1])
    lst.pop(-1)
    s_count -= 1
