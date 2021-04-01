class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        arr = list(map(int, s))
        # print(arr)
        n = [(arr[i], i) for i in range(0, len(arr))]
        n = sorted(n, key=lambda x:(-x[0],-x[1]))
        #print(n)
        j = 0
        for i in range(0, len(arr)):
            #print(i, j)
            curr = arr[i]
            
            curr_max = n[j][0]
            curr_max_pos = n[j][1]
            
            if curr_max_pos < i:
                while curr_max_pos < i:
                    j += 1
                    curr_max = n[j][0]
                    curr_max_pos = n[j][1]
            
            if curr < curr_max:
                # swap
                max_index = n[j][1]
                arr[i], arr[max_index] = arr[max_index], arr[i]
                break
          
            
        #print(arr)
        return ''.join(map(str, arr))
            
                
        
