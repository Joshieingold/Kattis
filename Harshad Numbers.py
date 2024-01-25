n = int(input())
while n % sum(int(digit) for digit in str(n)) != 0:
    n += 1
print(n)
