def locate_smallest(A):
    B = sorted(A)
    print(B)
    left = 0
    while left < len(A) and B[left] == A[left] :
        left += 1
    right = len(A) - 1
    while right > 0 and B[right] == A[right]:
        right -= 1
    return [left, right]
A = [3, 7, 5, 6, 9]
print(locate_smallest(A))