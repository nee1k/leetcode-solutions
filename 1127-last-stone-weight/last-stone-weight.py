class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:            
            x = max(stones)
            stones.remove(x)

            y = max(stones)
            stones.remove(y)

            diff = abs(x-y)

            if diff != 0:
                stones.append(diff)
        
        return stones[0] if stones else 0

        