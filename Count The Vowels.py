string = input()
count = 0
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        count += 1
print(count)
