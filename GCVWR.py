line_1 = input()
g,t,n = line_1.split(" ")
g = int(g)
t = int(t)
n = int(n)
mid = g-t
do_not_exceed = mid*0.9
i = input()
i = i.split(" ")
added = 0
for item in i:
    added += int(item)
final = (do_not_exceed - added)
print(int(final))

#1. line_1 is just grabbing the inputs and storing them in a variable
#2. then we take the values we got in line_1 and split them into 3 separate variables
#3. we make g an int
#4. we make t an int
#5. we make n an int
#6. Then we store g - t in a variable which is part of the problems requirements
#7. then we put 90% of do_not_exceed into a variable and that is basically the first set of inputs delt with
#9. Now we put the inputs we need to add into a variable
#10. We split it up and store it into a list.
#11. I make "added" into a place we can store our numbers for a loop
#12. Now we make item, and will be looped through for each thing in the list "i"
#13. so added becomes added + item and that will make it so its going to add one per the list.
#14. final then becomes our do_not_exceed number - the numbers we added from our second input
#15. I had to print it as an int instead of a float so this is what that is.