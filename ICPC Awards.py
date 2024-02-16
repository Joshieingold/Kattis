count = int(input())
winner_teams = []
university_lst = []
while count > 0:
    university, team_name = input().split(" ")
    if university not in university_lst:
        university_lst.append(university)
        winner_teams.append(university + " " + team_name)
    else:
        pass
    count -= 1
for i in range(12):
    print(winner_teams[i])