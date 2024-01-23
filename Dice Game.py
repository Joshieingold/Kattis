data = []
data += map(int, input().split(" "))
data += map(int, input().split(" "))
gunnar = sum(data[:4])
emma = sum(data[4:])
if gunnar > emma:
    print("Gunnar")
elif gunnar < emma:
    print("Emma")
else:
    print("Tie")
