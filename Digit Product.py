initial = str(input())
def multiply_memes(initial):
    lst = [int(char) for char in initial if char != '0']
    product = 1
    for num in lst:
        product *= num
    return str(product)
while len(initial) != 1:
    initial = multiply_memes(initial)

print(initial)