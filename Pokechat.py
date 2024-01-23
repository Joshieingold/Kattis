text = input()
cypher = input()
cypher_len = len(cypher)
cypher_lst = []
int_cypher_lst = []
pi, ka, chu = 0, 1, 2
while cypher_len > 0:
    x = cypher[pi] + cypher[ka] + cypher[chu]
    cypher_lst.append(x)
    pi += 3
    ka += 3
    chu += 3
    cypher_len -= 3
for num in cypher_lst:
    int_cypher_lst.append(int(num))
final = ""
count = len(int_cypher_lst)
for num in int_cypher_lst:
    final += text[num - 1]
print(final)


