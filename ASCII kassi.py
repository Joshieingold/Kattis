n = int(input())
count = n + 2
extra_count = count
lst = []
lst += range(n+2)
image = []
while count > 0:
    if count == n + 2:
        print("+" + ("-" * n) + "+")
    elif count == 1:
        print("+" + ("-" * n) + "+")
    else:
        print("|" + (" " * n) + "|")
    count -= 1
# Game plan:
    # First need to make it so if its the first line ie ( = our counts inital number) then it prints "+" ("-" n - 2 times) "+"
    # Then if i == range min(lst) print "|" "" n - 2 times, "|"
    # Then if count = 1, print "+" ("-" n - 2 times) "+"
#print(lst)