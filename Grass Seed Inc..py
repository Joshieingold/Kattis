cost = float(input())
num_lawn = int(input())
total_price = 0
count = num_lawn
while count > 0:
    in3 = input()
    width, length = in3.split(" ")
    width = float(width)
    length = float(length)
    multiplied = (width*length)
    total_price += multiplied * cost
    count -= 1
print(total_price)

