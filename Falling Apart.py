num_pieces = int(input())
piece_lst = list(map(int, input().split(" ")))
alice_turn = True
alice = 0
bob = 0
while num_pieces > 0:
    choice = max(piece_lst)
    piece_lst.pop(piece_lst.index(choice))
    if alice_turn == True:
        alice += int(choice)
        alice_turn = False
        num_pieces -= 1
    elif alice_turn == False:
        bob += int(choice)
        alice_turn = True
        num_pieces -= 1
print(alice, bob)

