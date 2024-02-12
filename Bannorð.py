forbidden = input()
forbidden = [*forbidden]
text = input()
text_lst = text.split(" ")
screwed_lst = []
final_lst = []
final = ""
for letter in forbidden:
    for word in text_lst:
        if letter in word:
            screwed_lst.append(word)
        else:
            pass
for i in text_lst:
    if i in screwed_lst:
        final_lst.append("*" * len(i))
    else:
        final_lst.append(i)
for i in final_lst:
    final += i + " "
print(final)