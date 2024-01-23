line_1 = input()
num_hands, dom_suit = line_1.split(" ")
num_hands = int(num_hands) * 4
points = 0

while num_hands > 0:
    hand = input()
    if dom_suit in hand:
        if "A" in hand:
            points += 11
        elif "K" in hand:
            points += 4
        elif "Q" in hand:
            points += 3
        elif "J" in hand:
            points += 20
        elif "T" in hand:
            points += 10
        elif "9" in hand:
            points += 14
        elif "8" in hand:
            points += 0
        elif "7" in hand:
            points += 0
        #print(points)
    else:
        if "A" in hand:
            points += 11
        elif "K" in hand:
            points += 4
        elif "Q" in hand:
            points += 3
        elif "J" in hand:
            points += 2
        elif "T" in hand:
            points += 10
        elif "9" in hand:
            points += 0
        elif "8" in hand:
            points += 0
        elif "7" in hand:
            points += 0
        #print(points)
    num_hands -= 1
    #print(num_hands)
print(points)

