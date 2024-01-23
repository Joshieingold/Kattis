line_1 = input()
gold, silver, copper = line_1.split(" ")
gold, silver, copper = int(gold), int(silver), int(copper)
buy_power = (gold * 3) + (silver * 2) + (copper * 1)
extra = 1
province = 8
duchy = 5
estate = 2
if buy_power >= province:
    dom_choice = "Province"
elif buy_power >= duchy:
    dom_choice = "Duchy"
elif buy_power >= estate:
    dom_choice = "Estate"
else:
    extra = 0
gold_buy = 6
silver_buy = 3
copper_buy = 0
if buy_power >= gold_buy:
    treasure_choice = "Gold"
elif buy_power >= silver_buy:
    treasure_choice = "Silver"
elif buy_power >= copper_buy:
    treasure_choice = "Copper"
if extra > 0:
    print(str(dom_choice), "or", str(treasure_choice))
else:
    print("Copper")