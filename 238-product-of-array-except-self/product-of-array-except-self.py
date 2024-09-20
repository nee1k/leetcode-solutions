class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        prefix.append(1)

        suffix = [1] * (len(nums) + 2)
        for i in range(len(nums)-1, -1, -1):
            suffix[i+1] = suffix[i+2] * nums[i]
                
        res = []
        for i in range(1, len(prefix)-1):
            res.append(prefix[i-1] * suffix[i+1])
        
        return res






