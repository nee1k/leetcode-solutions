class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stack = []

        while i < len(popped):
            to_pop = popped[i]

            while to_pop not in stack and len(stack) < len(pushed):
                stack.append(pushed[j])
                j += 1
            
            if stack[-1] != to_pop:
                return False
            
            stack.pop()
            i += 1
        
        return True

        