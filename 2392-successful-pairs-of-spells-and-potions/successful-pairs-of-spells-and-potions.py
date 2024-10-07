class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for spell in spells:
            count = 0
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = l+(r-l)//2

                if spell * potions[m] >= success:
                    count += (r - m + 1) 
                    r = m - 1
                else:
                    l = m + 1
                
            res.append(count)

        return res
                
        