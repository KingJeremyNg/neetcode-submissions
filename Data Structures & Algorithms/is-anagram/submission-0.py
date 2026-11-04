class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicString = {}
        dicTarget = {}
        for i in range(len(t)):
            if s[i] not in dicString:
                dicString[s[i]] = 1
            else:
                dicString[s[i]] += 1
            if t[i] not in dicTarget:
                dicTarget[t[i]] = 1
            else:
                dicTarget[t[i]] += 1
        return dicString == dicTarget
