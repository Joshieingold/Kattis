count = int(input())
while count > 0:
    line_1 = input()
    line_2 = input()
    crypto_1 = list(line_1)
    crypto_2 = list(line_2)
    check = 0
    detail = ""
    for num in crypto_1:
        if crypto_1[check] == crypto_2[check]:
            detail += "."
        else:
            detail += "*"
        check += 1
    print(line_1)
    print(line_2)
    print(detail)
    print("")
    count -= 1