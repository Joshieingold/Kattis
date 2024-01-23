# num of tasks, num of mins we can complete tasks in
# mins the task takes
tasks, test_mins = input().split(" ")
count = 0
min_count = 0
individual_task_lst = list(map(int, input().split(" ")))
for i in individual_task_lst:
    if int(i) + min_count <= int(test_mins):
        min_count += int(i)
        count += 1
    else:
        break
print(count)