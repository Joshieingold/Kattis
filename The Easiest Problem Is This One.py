logic = False
while logic == False:
    m = int(input())
    if m == 0:
        logic = True
    else:
        test = 11
        count = 0
        search = 0
        searching_for = list(str(m))
        for j in searching_for:
            search += int(j)

        found = False
        while not found:
            test_lst = list(str(m * test))
            for i in test_lst:
                count += int(i)
            if count == search:
                print(test)
                test = 11
                count = 0
                search = 0
                found = True
            else:
                test += 1
                count = 0
'''Chat GPT Condensed version
while (m := int(input())) != 0:
    search = sum(map(int, str(m)))
    test = 11
    while sum(map(int, str(m * test))) != search:
        test += 1
    print(test)
'''