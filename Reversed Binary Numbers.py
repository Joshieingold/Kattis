# Gets our number into binary
num = int(input())
binary = str(bin(num))
if "0b" in binary:
    useless, binary = binary.split("0b")
# Reverses our binary number
rev = binary[::-1]
print(int(rev, 2))
