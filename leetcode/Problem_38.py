class Solution:
    def countAndSay(self, n: int) -> str:
        k = 0
        s = ""
        while k < n:
            if k == 0:
                s = "1"  # base case
            else:
                arr = list(s)
                count = 0
                prev = arr[0]
                res = ""
                for i in range(0, len(arr)):
                    #print(arr[i], prev)
                    if arr[i] == prev:
                        count += 1
                    else:
                        res += str(count) + prev
                        #print(res)
                        count = 1
                        prev = arr[i]
                if count > 0:
                    res += str(count) + prev
                    
                s = res
                    
            k += 1
        return s
