blocks = int(input())
counter = 1
layers = 0
while blocks > 0:
    blocks -= counter**2
    counter += 2
    if blocks < 0:
        break
    else:
        layers += 1
print(layers)