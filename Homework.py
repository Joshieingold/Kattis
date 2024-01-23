lst = input().split(";")
problems = 0
for question in lst:
    if "-" in question:
        math = question.split("-")
        math[0] = int(math[0])
        math[1] = int(math[1])
        problems += int(math[1]) - int(math[0]) + 1
    else:
        problems += 1
print(problems)