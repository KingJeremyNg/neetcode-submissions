class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charSet = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in charSet:
                if stack and stack[-1] == charSet[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        return True
