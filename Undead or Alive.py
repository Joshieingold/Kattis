text = input()
if ":(" in text:
    if ":)" in text:
        state = "double agent"
    else:
        state = "undead"
elif ":)" in text:
    state = "alive"
else:
    state = "machine"
print(state)
