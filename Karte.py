# Getting the Data and setting up variables.
hand_raw = input()
num_cards = int(len(hand_raw) / 3)
count = num_cards
hand = []
next = 0
double = False
p = 13
k = 13
h = 13
t = 13

# Getting a split up list with the cards and their suit.
while count > 0:
    card = ""
    for i in range(3):
        card += hand_raw[next]
        next += 1
    hand.append(card)
    count -= 1

# Check if there are two exact cards in the deck.
for i in hand:
    if hand.count(i) > 1:
        double = True

# Finding our outputs and math on the number of cards left.
if double == True:
    print("GRESKA")
elif double == False:
    for i in hand:
        if str(i)[0] == "P":
            p -= 1
        elif str(i)[0] == "K":
            k -= 1
        elif str(i)[0] == "H":
            h -= 1
        elif str(i)[0] == "T":
            t -= 1
    print(p, k, h, t)
