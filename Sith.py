name = input()
num_1 = int(input())
num_2 = int(input())
answer = int(input())
correct_answer = num_1 - num_2
if correct_answer < 0:
    if answer < 0:
        print("JEDI")
    else:
        print("SITH")
else:
    print("VEIT EKKI")