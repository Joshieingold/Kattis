dice_1, dice_2 = map(int, input().split(" "))
one_lst = []
two_lst = []
lst = []
answer = 0
answer_lst = []
justin_gay = False
if dice_1 < 4 or dice_1 > 20:
    justin_gay = True
if dice_2 < 4 or dice_2 > 20:
    justin_gay = True
if justin_gay == False:
    for i in range(1, dice_1 + 1):
        one_lst.append(i)
    for j in range(1, dice_2 + 1):
        two_lst.append(j)
    for x in one_lst:
        for y in two_lst:
            lst.append(int(x) + int(y))
    lst.sort()
    answer = lst[0]

    for m in lst:
        if lst.count(m) > answer:
            answer = lst.count(m)

    for m in lst:
        if lst.count(m) == answer:
            answer_lst.append(m)

    answer_lst = list(set(answer_lst))
    for s in answer_lst:
        print(s)


