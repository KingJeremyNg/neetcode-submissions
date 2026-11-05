class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in ans:
                ans[sortedString].append(string)
            else:
                ans[sortedString] = [string]
        result = []
        for arr in ans.values():
            result.append(arr)
        return result
