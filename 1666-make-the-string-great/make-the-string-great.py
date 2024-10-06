class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(0, len(s)):
            if not stack:
                stack.append(s[i])
                continue

            print(s[i], stack)
            if s[i] != stack[-1] and (s[i].lower() == stack[-1] or s[i].upper() == stack[-1]):
                stack.pop()
                i += 1
            
            else:
                stack.append(s[i])


            print(stack)

        res = ""
        for char in stack:
            res += char
        return res