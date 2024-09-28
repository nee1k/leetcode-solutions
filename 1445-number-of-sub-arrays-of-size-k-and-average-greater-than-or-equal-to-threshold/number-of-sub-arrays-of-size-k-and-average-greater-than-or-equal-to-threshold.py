class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curr_sum = sum(arr[:k-1])
        threshold *= k

        for l in range(len(arr) - k + 1):
            r = l + k - 1
            curr_sum += arr[r]

            if curr_sum >= threshold:
                count += 1
            
            curr_sum -= arr[l]

        return count
        