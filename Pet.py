count = 1
lst = []
score = 0
time = 0
while count < 6:
    line = input()
    a, b, c, d = line.split(" ")
    a, b, c, d = int(a), int(b), int(c), int(d)
    new_score = a + b + c + d
    if score < new_score:
        score = new_score
        time = count
    count += 1
print(time, score)