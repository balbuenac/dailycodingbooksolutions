import heapq

def ugly_numbers(n, primes):
    nums = primes.copy()
    heapq.heapify(nums)
    p = 1
    for i in range(n-1):
        p = heapq.heappop(nums)
        for prime in primes:
            heapq.heappush(nums, p*prime)
            if p % prime == 0:
                break

    return p

n = 16
primes = [2,3,5]
print(ugly_numbers(n, primes))
