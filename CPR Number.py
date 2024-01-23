#6-dob 4 sequence num
#
cpr_num = input()
lst = [int(digit) for digit in cpr_num if digit.isdigit()]
#print(lst)
total_num = 0
total_num += lst[0] * 4
total_num += lst[1] * 3
total_num += lst[2] * 2
total_num += lst[3] * 7
total_num += lst[4] * 6
total_num += lst[5] * 5
total_num += lst[6] * 4
total_num += lst[7] * 3
total_num += lst[8] * 2
total_num += lst[9] * 1
#print(total_num / 11)
check = total_num / 11
if check != int(check):
    print(0)
else:
    print(1)