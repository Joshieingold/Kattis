count = int(input())
answer = 0
while count > 0:
    line_1 = input()
    compressed = str(line_1)
    power_location = (len(compressed) - 1)
    power = int((compressed[power_location]))
    num = int(compressed[:-1])
    answer += num ** power
    count -= 1
print(answer)