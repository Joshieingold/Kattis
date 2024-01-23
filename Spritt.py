#line 1 is number of classrooms and how many bottles availible
# then n lines which is (i) how many bottles the classroom needs.

# This deals with Line input one and makes them all integers
line_1 = input()
classr, bottles = line_1.split(" ")
#classr = int(classr)
bottles = int(bottles)
# Now I need to store n number of lines and sum them up.
count = int(classr)
total = 0
while count > 0:
    added = input()
    added = int(added)
    total = added + total
    count -= 1
# now we see if total needed can be given to everyone
if bottles/total < 1:
    print("Neibb")
else:
    print("Jebb")
