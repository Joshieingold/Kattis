# first input is the number of cases
# second is the number of places
# We need to output the amount of unique places per list of places
cases = int(input())
while cases > 0:
    count = int(input())
    lst = []
    unique = 0
    while count > 0:
        location = input()
        if location in lst:
            Josh = 1
        else:
            lst.append(location)
        count -= 1
    for x in lst:
        unique += 1
    print(unique)
    cases -= 1



