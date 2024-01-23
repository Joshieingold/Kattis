# first line is number of hotels they own
# the distance of the hotels they own from you
# possible roles = 36
num_hotels = int(input())
hotel_distance = input().split(" ")
total_probability = 0
for spec_hotel in hotel_distance:
    spec_hotel = int(spec_hotel)
    if spec_hotel <= 7:
        num_probability = spec_hotel - 1
    elif spec_hotel == 8:
        num_probability = 5
    elif spec_hotel == 9:
        num_probability = 4
    elif spec_hotel == 10:
        num_probability = 3
    elif spec_hotel == 11:
        num_probability = 2
    else:
        num_probability = 1
    #print( num_probability)
    total_probability += num_probability / 36
    #print(total_probability)
print(total_probability)