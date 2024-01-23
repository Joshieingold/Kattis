# Num of knots needed to be learned
# The knots he needs to learn
# The knots learned so far
# You output the number that is not used
num_knots = int(input())
knots_n_list = []
knots_n_list = input().split(" ")
knots_l_list = []
knots_l_list += input().split(" ")
while num_knots > 0:
    if knots_n_list[-1] in knots_l_list:
        knots_n_list.pop(-1)
        num_knots -= 1
    else: num_knots -= 1
print(int(knots_n_list[-1]))