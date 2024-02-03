timer = int(input())
test_lst = []
while timer > 0:
    test_lst.append(input())
    timer -= 1
inc_lst = sorted(test_lst)
dec_lst = sorted(test_lst, reverse=True)
if test_lst == inc_lst:
    print("INCREASING")
elif test_lst == dec_lst:
    print("DECREASING")
else:
    print("NEITHER")