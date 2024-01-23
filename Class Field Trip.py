ann = input()
ben = input()
combined = ann + ben
lst = (sorted(combined))
new_string = ""
for i in lst:
    new_string += i
print(new_string)
