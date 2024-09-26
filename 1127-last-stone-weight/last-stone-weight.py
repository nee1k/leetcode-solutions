class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            diff = abs(x-y)

            if diff != 0:
                stones.append(diff)
        
        return stones[0] if stones else 0

        