answer = input()
answer_lst = []
for i in answer:
    answer_lst.append(i)
guess = input()
die = 0
for i in guess:
    if i in answer_lst:
        for j in range(answer_lst.count(i)):
            answer_lst.remove(i)
    else:
        die += 1
    if die == 10:
        print("LOSE")
        break
    if answer_lst == []:
        print("WIN")
        break