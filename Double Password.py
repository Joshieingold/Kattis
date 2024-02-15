# Getting Inputs
passwordA = [*input()]
passwordB = [*input()]
multiply_lst = []
num = 1

# checks the amount of possibilities

for i in range(4):
    if passwordA[i] == passwordB[i]:
        multiply_lst.append(int(1))
    elif passwordA[i] != passwordB[i]:
        multiply_lst.append(int(2))


# multiply them one by one

for i in multiply_lst:
    num = num * i
print(num)