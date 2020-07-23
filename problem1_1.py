A = [1, 2, 3, 4, 5]
N = len(A)
B = [1] * N
prev, next = 1, 1
for i in range(0, N):
    B[i] = prev
    prev = prev * A[i]
print(B)
for i in range(N-1, -1, -1):
    B[i] = B[i] * next
    next = next * A[i]
print(B)
