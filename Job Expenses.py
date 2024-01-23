cases = int(input())
numbers = input()
lst = []
add = 0
lst += numbers.split(" ")
while cases > 0:
    if int(lst[-1]) < 0:
        add += int(lst[-1]) * -1
        lst.pop(-1)
        cases -= 1
    else:
        lst.pop(-1)
        cases -= 1
print(add)