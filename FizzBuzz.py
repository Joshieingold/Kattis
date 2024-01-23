line_1 = input()
x, y, n = line_1.split(" ")
x = int(x)
y = int(y)
n = int(n)
n += 1
lst = range(1, n)
for item in lst:
    if item % x == 0:
        if item % y == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif item % y == 0:
        print("Buzz")
    else:
        print(item)
