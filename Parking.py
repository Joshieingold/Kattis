test_cases = int(input())
while test_cases > 0:
    num_stores = int(input())
    lst = input().split(" ")
    real_lst = []
    for i in lst:
        real_lst.append(int(i))
    print((max(real_lst) - min(real_lst)) * 2)
    test_cases -= 1
