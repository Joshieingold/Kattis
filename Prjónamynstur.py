# . = 20, (CAP) O = 10, \ = 25, / = 25, A = 35, ^ = 5, (lowercase) v = 22
# input 1 is row, things in row
row, colum = map(int, input().split(" "))
yarn = 0
for i in range(row):
    string = input()
    for j in range(colum):
        if string[j] == ".":
            yarn += 20
        elif string[j] == "O":
            yarn += 10
        elif string[j] == "\\":
            yarn += 25
        elif string[j] == "/":
            yarn += 25
        elif string[j] == "A":
            yarn += 35
        elif string[j] == "^":
            yarn += 5
        elif string[j] == "v":
            yarn += 22
print(yarn)
