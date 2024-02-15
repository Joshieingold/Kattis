count = int(input())
while count > 0:
    question = input()
    if question == "P=NP":
        print("skipped")
        count -= 1
    else:
        a, b = question.split("+")
        print(int(a)+int(b))
        count -= 1