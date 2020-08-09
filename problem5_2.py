# data
A = [[3, 5, 1, 1], [2, 3, 3, 2], [5, 5], [4, 4, 2],[1, 3, 3, 3], [1, 1, 6, 1, 1]]
# solution
h = {}
total_sum = 0
for i in range(0, len(A)):
    row = A[i]
    j = 0
    sum_row = 0
    while j < len(row):
        sum_row += A[i][j]
        if sum_row not in h:
            h[sum_row] = 0
        h[sum_row] += 1
        j = j + 1
    if total_sum == 0:
        total_sum = sum_row

if total_sum in h: # delete right-most sum as it wont cut any brick as it is the end
    del h[total_sum]
print(h)
min_cut = max(h.values())
result = len(A) - min_cut
print(result)