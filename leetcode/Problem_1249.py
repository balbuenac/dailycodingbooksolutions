class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openstack = []
        toremove = {i:False for i in range(0, len(s))}
        for i in range(0, len(s)):
            if s[i] == '(':
                openstack.append(i)
            elif s[i] == ')':
                if openstack:
                    openstack.pop(0)
                else:
                    toremove[i] = True
        while openstack:
            toremove[openstack.pop(0)] = True

        result = ""
        for i in range(0, len(s)):
            if toremove[i] == False:
                result += s[i]

        return result

