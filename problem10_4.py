from collections import deque

def helper(snakes, ladders):
    paths = {**snakes, **ladders}
    start, end = 0, 100

    q = deque()
    q.append((start, 0))
    visited = set()
    while q:
        s, turn = q.popleft()
        for move in (s+1, s+7):

            if move > end:
                return turn + 1

            if not move in visited:
                visited.add(move)
                if move in paths:
                    next_move = paths[move]
                    q.append((next_move, turn+1))

    return 0
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
print(helper(snakes, ladders))