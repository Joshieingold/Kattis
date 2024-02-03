width_cake = int(input())
num_pieces = int(input())
total_cake = 0
while num_pieces > 0:
    l, w = map(int, (input().split(" ")))
    piece = l * w
    total_cake += piece
    num_pieces -= 1
print(int(total_cake / width_cake))

