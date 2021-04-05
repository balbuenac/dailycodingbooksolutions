def Reversort(L):
        cost = 0
        for i in range(0, len(L)):
        j = helper(L, i)
        Reverse(L, i, j)
        print(L)
        cost = (j+1) - (i+1)  + 1

        return cost

def Reverse(L, i, j):
        L[i:j] = L[i:j][::-1]
    
def helper(L, i):
        min_val =  min(L[i:])		
        for i in range(i, len(L)):
                if L[i] == min_val:
                        return i
        return -1

print(Reversort([4, 2, 1, 3]))
