cases = int(input())
count = 1
while count <= cases:
    guests = input()
    line_1 = input()
    lst = line_1.split(" ")
    #print(lst)
    for i in lst:
        test = lst.count(i)
        if test < 2:
            print("Case #" + str(count) + ":", i)
    count += 1