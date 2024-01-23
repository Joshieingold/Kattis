x = int(input())
y = int(input())
if x>0 and y>0:
    Answer = 1
    print (Answer)
elif x<0 and y>0:
    Answer = 2
    print (Answer)
elif x<0 and y<0:
    Answer = 3
    print (Answer)
else:
    Answer = 4
    print (Answer)
# 1 = both pos, 2 = neg x and pos y, 3 = both neg, 4 = pos x neg y.