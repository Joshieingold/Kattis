string = input()
lst = list(map(str, string))
even_count = 0
for x in lst:
    if lst.count(x) % 2 == 0:
        even_count += 1
if even_count <= 1:
    print(1)
else:
    print(0)