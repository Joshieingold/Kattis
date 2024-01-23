num_server = int(input())
cpu_full = 0
memory_full = 0
hard_drive_full = 0
total = 0
for i in range (num_server):
    cpu, memory, hard_drive = input().split(" ")
    if "J" in cpu:
        cpu_full += 1
    if "J" in memory:
        memory_full += 1
    if "J" in hard_drive:
        hard_drive_full += 1
while cpu_full and memory_full and hard_drive_full >= 1:
    total += 1
    cpu_full -=1
    memory_full -= 1
    hard_drive_full -= 1
print(total)