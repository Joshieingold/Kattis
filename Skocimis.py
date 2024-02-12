def find(a, b, c):
    if b - a == 1 and c - b == 1:
        return 0
    elif b - a == 1:
        return 1 + find(b, b + 1, c)
    elif c - b == 1:
        return 1 + find(a, b - 1, b)
    else:
        return 1 + max(find(b, b + 1, c), find(a, b - 1, b))

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    n = find(a, b, c)
    print(n)