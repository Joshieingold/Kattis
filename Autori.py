s=input()
a = s.split("-")
answer = ""
for name in a:
    answer = answer + name[0]
print(answer)



#1. I am assigning a variable to the input (s)
#2. I am splitting (s) and assigning that to a variable
#3. I have answer as blank, this way it is nothing that I can loop off
#4. I create the variable "name", saying for each name in "a" we will do this,
#5. Then inside of that perameter I say nothing = the first letter of everything in "a"
#6. If inside the loop I print then it will show all idorations so I put it outside the loop that way I can only get the final result.