# Opening Conditions

o_win = None
full_lst = []

# Getting the inputs as well as checking the horizontal lines for a win while were at it

for i in range(3):
    line = input()
    line_lst = []
    for j in line:
        line_lst.append(j)
        full_lst.append(j)
    if line_lst[0] == "O" and line_lst[1] == "O" and line_lst[2] == "O":
        o_win = True

# Checking vertical and diagonal lines for a win.

if full_lst[0] == "O" and full_lst[3] == "O" and full_lst[6] == "O":
    o_win = True
elif full_lst[1] == "O" and full_lst[4] == "O" and full_lst[7] == "O":
    o_win = True
elif full_lst[2] == "O" and full_lst[5] == "O" and full_lst[8] == "O":
    o_win = True
elif full_lst[0] == "O" and full_lst[4] == "O" and full_lst[8] == "O":
    o_win = True
elif full_lst[6] == "O" and full_lst[4] == "O" and full_lst[2] == "O":
    o_win = True

# Finding the winner

if o_win == True:
    print("Jebb")
else:
    print("Neibb")
