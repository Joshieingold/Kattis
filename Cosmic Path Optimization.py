m = int(input())
temps = list(map(int, input().split(" ")))
s_temp = sum(temps)
print(int(s_temp / m))