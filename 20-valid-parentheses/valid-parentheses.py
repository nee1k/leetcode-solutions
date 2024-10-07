class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")",
                "{": "}",
                "[": "]"}
        stack = []

        for i in range(0, len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])

            elif stack and pairs[stack[-1]] == s[i]:
                stack.pop()
            
            else:
                return False
            
        return True if not stack else False        