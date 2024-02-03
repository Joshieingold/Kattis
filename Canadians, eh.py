text = input()
eh_look_up = len(text)
eh_look_up -= 3
canada_check = ""
count = 3
while count > 0:
    canada_check += text[eh_look_up]
    eh_look_up += 1
    count -= 1
if canada_check == "eh?":
    print("Canadian!")
else:
    print("Imposter!")