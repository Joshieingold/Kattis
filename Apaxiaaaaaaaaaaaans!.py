string = input()
output = []
count = 0
for letter in string:
    if len(output) < 1:
        output.append(letter)
    elif len(output) >= 1:
        if letter == output[-1]:
            count += 1
        else:
            output.append(letter)
print("".join(output))
# This will tell you how many letters were deleted for no reason lol.
#print(count)