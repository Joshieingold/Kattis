less_than = int(input())
full_lst = []
for a in range(1, less_than + 1):
    answer = a * (a+1) * (a+2)
    if answer < less_than:
        full_lst.append(answer)
    else:
        break
print(len(full_lst))