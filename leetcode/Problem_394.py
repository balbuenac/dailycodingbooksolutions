class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            #print("la cadena " + s)
            if len(s) == 0:
                return ""
            if s[0].isalpha():
                t, i = "", 0
                while i < len(s) and s[i].isalpha():
                    t+=s[i]
                    i+=1
                return t + helper(s[i:])
            elif s[0].isdigit():
                t, i = "", 0
                while i < len(s) and s[i].isdigit():
                    t+=s[i]
                    i+=1
                new_s = ""
                #print(s, i)
                i = i + 1 # skip [
                countOpen, countClose = 1, 0
                while i < len(s) and countOpen != countClose:
                    new_s += s[i]
                    if s[i] == '[':
                        countOpen += 1
                    elif s[i] == ']':
                        countClose += 1
                    i += 1
                #print(new_s)
                #new_s = new_s[:]
                new_s = new_s[:-1] # remove last ]
                #print(s, i, new_s, s[i:])
                res = ""
                repeat = helper(new_s)
                for _ in range(0, int(t)):
                    res += repeat
                res += helper(s[i:])
                return res
            return ""

        if len(s) == 0:
            return ""
        return helper(s)1
