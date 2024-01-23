# The number of test cases
# for the number of test cases is N, it will be less than 10:
test_cases = int(input())
lst = []
final = 1
while test_cases > 0:
    n = int(input())
    for num in range(n):
        lst.append(num + 1)
        #print(lst)
    test_cases -= 1
    for x in lst:
        final = final * x
    toast = (str(final)[-1])
    final = 1
    lst = []
    print(int(toast))
