left = 1
middle = 0
right = 0
string = input()
for char in string:
    if char == "A":
        void = left
        left = middle
        middle = void
        void = 0
    elif char == "B":
        void = middle
        middle = right
        right = void
    elif char == "C":
        void = right
        right = left
        left = void
        print(left, middle, right)
if left > 0:
    print(1)
elif middle > 0:
    print(2)
else:
    print(3)

