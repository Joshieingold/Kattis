text = input()
vowel_count = 0
vowel_lst = ["a", "e", "i", "o", "u"]
y_count = 0
for i in text:
    if i in vowel_lst:
        vowel_count += 1
    if i == "y":
        y_count += 1
print(vowel_count, vowel_count + y_count)