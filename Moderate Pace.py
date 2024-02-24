num_training_days = int(input())
josh_ideal = list(map(int, input().split(" ")))
justin_ideal = list(map(int, input().split(" ")))
tolga_ideal = list(map(int, input().split(" ")))
everyone_training_ideal = []
for i in range(num_training_days):
    lst = josh_ideal[i], justin_ideal[i], tolga_ideal[i]
    day_lst = sorted(lst)
    everyone_training_ideal.append(day_lst[1])
output = ""
for i in everyone_training_ideal:
    output += str(i) + " "
print(output)