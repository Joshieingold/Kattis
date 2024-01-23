compare = input()
num_1, num_2 = compare.split(" ")
num_1_count = 3
num_2_count = 3
num1_un = []
num1_un += num_1
num2_un = []
num2_un += num_2
num_1_flip = ""
num_2_flip = ""
while num_1_count > 0:
    num_1_flip += str(num1_un[-1])
    num1_un.pop(-1)
    num_1_count -= 1
while num_2_count > 0:
    num_2_flip += str(num2_un[-1])
    num2_un.pop(-1)
    num_2_count -= 1

if int(num_1_flip) > int(num_2_flip):
    choice = num_1_flip
else:
    choice = num_2_flip
# Now to swip swap em'
lst = []
lst += str(choice)
final = ""
count = 3
while count > 0:
    final += str(lst[0])
    lst.pop(0)
    count -= 1
print(int(final))