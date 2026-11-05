class Solution:
    whitespace = "*69*"
    separator = "*67*"

    def encode(self, strs: List[str]) -> str:
        encodedStrs = [self.whitespace if string == "" else string for string in strs]
        return self.separator.join(encodedStrs)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return ["" if string == self.whitespace else string for string in s.split(self.separator)]