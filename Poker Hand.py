hand = input().split(" ")
rank_lst = []
for i in hand:
    rank_lst.append(i[0])
pairs = 0
for j in rank_lst:
    if rank_lst.count(j) > pairs:
        pairs = rank_lst.count(j)
print(pairs)