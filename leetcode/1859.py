class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [''] * 10
        words = s.split(' ')
        max_index = -1
        for word in words:
            pos = int(word[len(word)-1])
            if pos > max_index:
                max_index = pos
            arr[pos] = word[:len(word)]
        result = []
        for i in range(1, max_index+1):
            w = arr[i]
            if len(w):
                if i == max_index:
                    result.append(w[:len(w)-1])
                else:
                    
                    result.append(w[:len(w)-1] + " ")
                    
        
        return ''.join(result)
