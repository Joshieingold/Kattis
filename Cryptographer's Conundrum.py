text = input()
count = 0
length = len(text)
#print (length)
divider = int(length / 3)
counter = 0
for i in range(divider):
    if text[0 + counter] == "P":
        count += 1
    if text[1 + counter] == "E":
        count += 1
    if text[2 + counter] == "R":
        count += 1
    #print(counter)
    counter += 3
print(length - count)