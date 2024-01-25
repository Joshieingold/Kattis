timer = int(input())
while timer > 0:
    phrase = input()
    if "Simon says" in phrase:
        simon, command = phrase.split("Simon says")
        print(command)
    timer -= 1