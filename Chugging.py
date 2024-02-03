num_bottles = int(input())
a_first_bottle, a_bottle_bonus = map(int, input().split(" "))
alice_time = 0
bob_time = 0
alice_time += a_first_bottle
for i in range(1, num_bottles):
    alice_time += a_first_bottle + (a_bottle_bonus * i)
b_first_bottle, b_bottle_bonus = map(int, input().split(" "))
bob_time += b_first_bottle
for i in range(1, num_bottles):
    bob_time += b_first_bottle + (b_bottle_bonus * i)
if bob_time < alice_time:
    print("Bob")
elif bob_time > alice_time:
    print("Alice")
elif bob_time == alice_time:
    print("=")