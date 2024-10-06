class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        for p, s in pair: # p = 10,8,5,3,0 s = 2,4,1,3,1 target = 12
            slope = (target - p) / s
            stack.append(slope) # [1.0, 1.0, 7.0, 3.0, 12.0]
            
            # [1.0]
            # [1.0, 1.0]
            # [1.0, 1.0, 7.0]
            # [1.0, 1.0, 7.0, 3.0]
            # [1.0, 1.0, 7.0, 3.0, 12.0]

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
            # [1.0]
            # [1.0]
            # [1.0, 7.0]
            # [1.0, 7.0]
            # [1.0, 7.0, 12.0]

        return len(stack)