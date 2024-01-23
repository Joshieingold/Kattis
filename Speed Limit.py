vex = True
prior_time = 0
while vex == True:
    count = int(input())
    total = 0
    if count == -1:
        vex = False
        break
    while count > 0:
        miles, time = map(int, input().split(" "))
        time -= prior_time
        total += miles * time
        prior_time += time
        count -= 1
    print(total, "miles")
    total = 0
    prior_time = 0