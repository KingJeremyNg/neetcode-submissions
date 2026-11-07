class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        result = 0
        left = 0
        right = 0
        uniques = set()

        while left <= right and left < len(s) and right < len(s):
            if s[right] not in uniques:
                uniques.add(s[right])
                result = max(result, len(uniques))
                right += 1
            else:
                uniques.remove(s[left])
                left += 1

        return result
