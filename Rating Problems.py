line_1 = input()
x, y = line_1.split(" ")
x = int(x)
y = int(y)
count = y
aojl = x - y
worst = aojl * -3
best = aojl * 3
total_score = 0
while count > 0:
    score = int(input())
    total_score += score
    count -= 1
best_total_score = total_score + best
worst_total_score = total_score + worst
print(worst_total_score / x, best_total_score / x)