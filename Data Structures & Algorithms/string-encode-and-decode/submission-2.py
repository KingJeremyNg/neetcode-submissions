class Solution:
    separator = "*69*"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 and strs[0] == "":
            return self.separator
        if not strs:
            return ""
        return self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == self.separator:
            return [""]
        return s.split(self.separator)
