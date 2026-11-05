class Solution:

    def encode(self, strs: List[str]) -> str:
        return "*69*".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        return s.split("*69*")
