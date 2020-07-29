def zigzag(S, k):
    m = [[' ' for x in range(len(S))] for y in range(k)]
    up, down = False, True
    col, row = 0, 0
    for i in range(0, len(S)):
        print(i, row, col)
        m[row][col] = S[i]
        if i % (k-1) == 0 and i > 0:
            up, down = not up, not down
            print(up, down)
        if down:
            row, col = row + 1, col + 1
        elif up:
            row, col = row - 1, col + 1
    for i in range(0, k):
        print("".join(m[i]))
S = "thisisazigzag"
k = 4
print(zigzag(S, k))