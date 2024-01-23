n = input()
n = int(n)
k = input().split(" ")
added = 0
for item in k:
    added += int(item)
print(added)


#1. We take the first input and keep it in variable n
#2. We then just make n into an integer
#3. Then take the next input and split it by " ", this will store it as a list
#4. We need something to store our added things to so its 0
#5. we make item and then every element in k we do whats under this
#6. so then we take added add it plus item and say thats what its equal to.
#7. Then we print added after it goes through the whole loop of everything in k