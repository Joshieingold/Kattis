# input 1 is the number of articles planned to publish
# input 2 is the impact number were planning to hit
line_1 = input()
art, impact = line_1.split(" ")
art = int(art)
impact = int(impact) - 1
almost = (art * impact)
print(almost + 1)
