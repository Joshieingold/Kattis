n, m = map(int, input().split(" "))
final = ""
for i in range(n):
    search = input()
    for j in range(m):
        if search[j] == ".":
            pass
        else:
            final += search[j]
print(final)