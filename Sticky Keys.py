line_1 = input()
final = []
for digit in line_1:
    if final == []:
        final.append(digit)
    elif digit != final[-1]:
        final.append(digit)
    else:
        pass
my_string = ""
for x in final:
    my_string += x
print(my_string)
