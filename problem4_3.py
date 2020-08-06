A = [10, 5, 2, 7, 8, 7]
k = 2
max_k = -1
n = len(A)
start, end = 0, 0
result_max_k = [0] * (n-k+1)
i = 0
while (start <= (n-k)):
    curr = A[end]
    if (end-start) == (k-1):
        result_max_k[i] = max(max_k, curr)
        i += 1
        max_k = -1
        start += 1
        end = start
    else:
        max_k = max(max_k, curr)
        end += 1
print(result_max_k)
