class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        sorted_nums_dict = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_nums_dict.keys())[:k]