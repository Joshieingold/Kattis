test_cases = int(input())
while test_cases > 0:
    possible = False
    x, y, answer = map(int, input().split(" "))
    # Add (1)
    if x + y == answer:
        possible = True
    # Mult (1)
    elif x * y == answer:
        possible = True
    # Sub (2)
    elif x - y == answer:
        possible = True
    elif y - x == answer:
        possible = True
    # div (2)
    elif x / y == answer:
        possible = True
    elif y / x == answer:
        possible = True
    else:
        print("Impossible")
    if possible == True:
        print("Possible")
    test_cases -= 1

