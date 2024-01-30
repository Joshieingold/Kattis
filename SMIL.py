text = input()
tracker_1 = 0
tracker_2 = 0
tracker_3 = 0
tracker_4 = 0
lst = []
for i in text:
    x = (text.find(":)", tracker_1, len(text)))
    if x >= 0:
        lst.append(x)
    tracker_1 += x + 1
for i in text:
    x = (text.find(":-)", tracker_2, len(text)))
    if x >= 0:
        lst.append(x)
    tracker_2 += x + 1
for i in text:
    x = (text.find(";)", tracker_3, len(text)))
    if x >= 0:
        lst.append(x)
    tracker_3 += x + 1
for i in text:
    x = (text.find(";-)", tracker_4, len(text)))
    if x >= 0:
        lst.append(x)
    tracker_4 += x + 1
for i in (sorted(lst)):
    print(i)