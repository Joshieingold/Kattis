l = str(input())
d = str(input())
x = int(input())
check = []

cases = int(d)
add = 0
output = []

while cases >= int(l):
    check += str(cases)
    for num in range(len(check)):
        add += int(check[0])
        check.pop(0)
    if add == x:
        output.append(cases)
    cases -= 1
    add = 0

print(output[-1])
print(output[0])