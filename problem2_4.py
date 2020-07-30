from heapq import *

def smallest_rotated_string(S, k):
    count_char = 0
    min_str = ''
    while count_char < len(S):
        heap = list(S[:k])
        remaining_string = S[k:]
        while heap:
            c = heappop(heap)
            remaining_string = remaining_string + c
            if len(remaining_string) == len(S):
                #print(remaining_string)
                if remaining_string < S:
                    min_str = remaining_string
                    break
        count_char += 1
    if min_str == '':
        min_str = S
    return min_str
S = "daily"
k = 1
print(smallest_rotated_string(S, k))

# O ( n logn )