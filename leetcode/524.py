class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''
        
        Edit Distance
        
        only delete operation 
        
        for w in dictionary:
            do_something(s)
        
        Maybe a Trie ? Pero hay busquedas ??
        
        Input:
            word    -   s
            dictionary of words -   dictionary
        
        Output:
            return the longest word with the smallest lexicographical order.
        
        
        Test Cases:
            it has only one result
            No result
            Multiple results
            
        s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
        
        build dictionary using S to save positions
        for w in words:
            for c in w:
                check in dictionary ?
        
        
        '''
        def is_match(s, w):
            i, j = 0, 0
            M , N = len(s), len(w)
            while i < M and j < N:
                while j < N and i < M and w[j] != s[i]:
                    i += 1
                if  j < N and i < M and w[j] == s[i]:
                    i += 1
                    j += 1
            
            return j == N
             
        results = []
        for w in dictionary:
            if is_match(s, w):
                results.append(w)
        # print(results)         
        results = list(results)
        results.sort(reverse=True)
        results.sort(key=len)


        return "" if not results else results[-1]
        
        
