pieces = input()
k, q, r, b, n, p = pieces.split()
k, q, r, b, n, p = int(k), int(q),int(r), int(b), int(n), int(p)
king_need = 0
queen_need = 0
rook_need = 0
bishop_need = 0
knight_need = 0
pawn_need = 0
while k < 1:
    k += 1
    king_need += 1
while k > 1:
    k -= 1
    king_need -= 1
while q < 1:
    q += 1
    queen_need += 1
while q > 1:
    q -= 1
    queen_need -= 1
while r < 2:
    r += 1
    rook_need += 1
while r > 2:
    r -= 1
    rook_need -= 1
while b < 2:
    b += 1
    bishop_need += 1
while b > 2:
    b -= 1
    bishop_need -= 1
while n < 2:
    n += 1
    knight_need += 1
while n > 2:
    n -= 1
    knight_need -= 1
while p < 8:
    p += 1
    pawn_need += 1
while p > 8:
    p -= 1
    pawn_need -= 1
print(king_need, queen_need, rook_need,bishop_need, knight_need, pawn_need)