initial_in_line = int(input())
line_lst = []
while initial_in_line > 0:
    line_lst.append(input())
    initial_in_line -= 1
num_actions = int(input())
while num_actions > 0:
    command = input().split(" ")
    if command[0] == "cut":
        insert = command[1]
        insert_index = command[2]
        line_lst.insert(line_lst.index(insert_index), insert)
    elif command[0] == "leave":
        leave = command[1]
        line_lst.pop(line_lst.index(leave))
    num_actions -= 1
for i in line_lst:
    print(i)