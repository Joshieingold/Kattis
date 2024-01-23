num_words = int(input())
words = input().split(" ")
final = ""
for word in words:
    if word[0].isupper() == True:
        final += (word[0])
    else:
        pass
print(final)
