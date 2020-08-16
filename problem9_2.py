from heapq import *

input = [('g', 1), ('g', 3), ('g', 5), ('p', 1), ('p', 2), ('b', 1), ('b', 3)]

pairs = {}
for pair in input:
    letter = pair[0]
    if not letter in pairs:
        pairs[letter] = set()
    pairs[letter].add(pair[1])
print(pairs)

sites = list(pairs.keys())
heap = []
for i in range(len(sites)):
    for j in range(i+1, len(sites)):
        len_users = len(pairs[sites[i]] | pairs[sites[j]])
        count_common = len(pairs[sites[i]] & pairs[sites[j]])
        heappush(heap, ((sites[i], sites[j]), count_common / len_users))
k = 2
for i in range(k):
    if heap:
        print(heappop(heap)[0])
