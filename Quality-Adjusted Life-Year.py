n = int(input())
count = int(n)
lst = []
while count > 0:
    i = input()
    q, y = i.split(" ")
    q = float(q)
    y = float(y)
    x = q*y
    lst.append(x)
    count -= 1
final = sum(lst)
print(final)

# I am aware this might be a slow way to do this but it works
#1. first I take the initial input and that will be the number of lines that will follow
#2. Then I make a count so my loop will run out based on the value inputted as n