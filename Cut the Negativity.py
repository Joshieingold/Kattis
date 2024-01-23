num_city = input()
x = 1
y = 1
count = int(num_city)
total_flights = []
total_inputs = []
while count > 0:
    line = input()
    banana = line.split(" ")
    total_inputs.extend(banana)
    for num in banana:
        if int(num) > 0:
            total_flights.append(int(num))
    count -= 1
print(len(total_flights))
for lst in total_inputs:
    if int(lst) > 0:
        print(y, x, lst)
        x += 1
        if x > int(num_city):
            x = 1
            y += 1
    else:
        x += 1
        if x > int(num_city):
            x = 1
            y += 1