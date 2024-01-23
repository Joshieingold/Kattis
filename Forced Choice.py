# num of cards, secret prediction, number of steps
# next number of step lines
# num of cards chosen, unique integers * num of cards chosen
count_cards, prediction, steps = map(int, input().split())
while count_cards > 1 and steps > 0:
    hand = list(map(int, input().split()))
    num_hand = hand[0]
    hand = set(hand[1:])
    if prediction in hand:
        print("KEEP")
    else:
        print("REMOVE")
        count_cards -= num_hand
    steps -= 1

