def knows(i, j):
    if i == 3:
        return False
    return True

def helper(v, i, n):
    for j in range(i+1, n):
        if v[j] == False:
            if knows(i,j):
                print(i, j)
                v[i] = True
                helper(v, j, n)

def findCelebrity(n):
    v = {i:False for i in range(0, n)}
    for i in range(0, n):
        helper(v, i, n)
    print(v)
    count, res = 0, -1
    for k, v in v.items():
        if v == False:
            res = k
            count += 1

    if count == 1:
        return res
    return -1

if __name__ == "__main__":
        n = 4
        findCelebrity(n)
