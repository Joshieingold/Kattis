lst = []
final = ""
for i in range(0, 5):
    text = input()
    if "FBI" in text:
        lst.append(i + 1)
if len(lst) > 0:
    for x in lst:
        final += str(x) + " "
    print(final)
else:
    print("HE GOT AWAY!")