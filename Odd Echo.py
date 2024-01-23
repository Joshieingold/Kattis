n = int(input())
lst = []
while n > 0:
    p = input()
    lst.append(p)
    n -= 1
    echo = (lst[::2])
print(*echo, sep = "\n")

#1. I am taking n and that will be the number of lines
#2. I create an empty list for my while loop to put things in
#3. I create a while loop that will end when n is 0
#4. I take any new inputs and store them as p
#5. I put anything that was p into my list on line 2.
#6. I take a counter off of n
#7. I take every second item in the list and store it in a new list. with a cool opperator "::2". I need to look into this.
#8. I print for every time in echo, "sep = \n" which I know lets me print every value on a seperate line but I dont understand what is really happening.