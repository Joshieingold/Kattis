n = input()
n = int(n)
y = int(n)
lst = []
while n != 0: 
  line = input()
  lst.append(int(line))
  n -=1
print(sum(lst)-(y-1))





#1. n = the first number and the number of idorations
#2. Then we cast n into an integer for sure
#3. Then we make n = to y to call it easier
#4. We create an empty list for the numbers.
#5. Then we create a loop that will keep going as long as the statement is true, in this case its while n is not equal to 0
#6. So then I take the numbers from my next input and put them into line
#7. Now since this is a loop we will keep adding to the list with integers every time we run through the loop.
#8. Then n -= 1 means we take away 1 from n everytime the loop idoerates.
#9. we print the sum of our list, and in this case we subtract y-1 because we want to subtract the first number from the sum.
