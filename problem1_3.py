def max_sum_subarray(A):
    N = len(A)
    curr, sum, max_sum = 0, 0, -1
    for i in range(0, len(A)):
        curr = A[i]
        if curr > max_sum:
            sum = curr
        else:
            sum += curr
        max_sum = max(curr, sum, max_sum)
    return max_sum
A = [34, -50, 42, 14, -5, 86]
print(max_sum_subarray(A))