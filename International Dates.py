num_1, num_2, year = map(int, input().split("/"))
if num_1 > 12:
    answer = "EU"
elif num_2 > 12:
    answer = "US"
elif num_1 <= 12 and num_2 <= 12:
    answer = ("either")
print(answer)