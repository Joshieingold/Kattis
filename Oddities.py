test_cases = int(input())
count = test_cases
while count > 0:
    num = int(input())
    if (num % 2) == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
    count -= 1