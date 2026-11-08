import string
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        characterSet = Counter(s1)

        while right <= len(s2):
            currentSet = Counter(s2[left:right])
            if characterSet == currentSet:
                return True
            left += 1
            right += 1

        return False
