def modulo_remainder(modulo, num):
    return num % modulo

modulo = 42
count = 0
lst = []
final_lst = set()

while count < 10:
    x = input()
    lst.append(x)
    count += 1

if len(lst) == 10:
    for item in lst:
        num = int(item)
        result = modulo_remainder(modulo, num)
        final_lst.add(result)

print(len(final_lst))