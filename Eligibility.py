'''
Rules:
1: If they began uni in 2010 or later, they're eligible.
2: If they are born in 1991 or later, they're eligible.
3: If the above doesn't apply & they have x > 8 classes, they're ineligible
4: If none of the above applies, then there is a petition.
'''

# Getting our data

cases = int(input())
while cases > 0:
    name, begin_uni, dob, courses = input().split(" ")
    courses = int(courses)
    eligible = None
    first_count = 4
    second_count = 4
    begin_uni_index = 0
    begin_life_index = 0

    # Checking for rule 1:

    begin_uni_year = ""
    while first_count > 0:
        begin_uni_year += begin_uni[begin_uni_index]
        begin_uni_index += 1
        first_count -= 1
    begin_uni_year = int(begin_uni_year)
    if begin_uni_year >= 2010:
        eligible = True

    # Checking for rule 2:

    if eligible == None:
        year_of_birth = ""
        while second_count > 0:
            year_of_birth += dob[begin_life_index]
            begin_life_index += 1
            second_count -= 1
        year_of_birth = int(year_of_birth)
        if year_of_birth >= 1991:
            eligible = True

        # Checking for rule 3:

        if eligible == None:
            if courses > 40:
                eligible = False
            else:
                print(name, "coach petitions")

    # Printing our output:
    if eligible == True:
        print(name, "eligible")
    elif eligible == False:
        print(name, "ineligible")
    cases -= 1

