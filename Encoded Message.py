import math
def divide_lst(sq, code):
    lst = []
    sq = int(sq)
    for i in range(0, len(code), sq):
        lst.append(code[i:i + sq])
    return lst
def decode():
    code = input()
    sq = len(code)
    sq = math.sqrt(sq)
    decoded = ""
    count = int(sq)
    lst = divide_lst(sq, code)
    element = (int(sq) - 1)
    while count > 0:
        for i in range(len(lst)):
            decoded += lst[i][element]

        element -= 1
        count -= 1

    print(decoded)
count = int(input())
while count > 0:
    decode()
    count -= 1





