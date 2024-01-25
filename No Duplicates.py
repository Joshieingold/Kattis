text_lst = input().split(" ")
count = 0
gold = False
for i in text_lst:
    if text_lst.count(i) > 1:
        gold = True
if gold == False:
    print("yes")
elif gold == True:
    print("no")