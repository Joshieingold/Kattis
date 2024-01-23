#input 1 = cases that will follow (while loop possible)
# for every input we get 3 lines:
    #rev = the estimated rev if no advertisement
    #expe = the expected rev if I do advertize
    #cost = the cost of advertising
count = int(input())
while count > 0:
    inp = input()
    rev, exp, cost = inp.split(" ")
    rev = int(rev)
    exp = int(exp)
    cost = int(cost)
    evc = exp - cost
    if rev > evc:
        print("do not advertise")
    elif evc > rev:
        print("advertise")
    else:
        print("does not matter")
    count -= 1