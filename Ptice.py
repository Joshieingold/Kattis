def ptice():
    A = ['A', 'B', 'C']
    B = ['B', 'A', 'B', 'C']
    C = ['C', 'C', 'A', 'A', 'B', 'B']

    n = int(input())
    l = list(input().strip())

    a, b, c = 0, 0, 0
    for i in range(n):
        if A[i % 3] == l[i]:
            a += 1
        if B[i % 4] == l[i]:
            b += 1
        if C[i % 6] == l[i]:
            c += 1

    max_count = max(a, b, c)
    print(max_count)

    if a == max_count:
        print("Adrian")
    if b == max_count:
        print("Bruno")
    if c == max_count:
        print("Goran")

if __name__ == "__main__":
    ptice()