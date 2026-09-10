class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        total_sum = 0
        L = 0

        for R in range(len(nums)):
            total_sum += nums[R]

            while total_sum >= target:
                length = min(R-L+1, length)
                total_sum -= nums[L]
                L += 1
        
        if length == len(nums) + 1:
            return 0
        else:
            return length
            
        
        
            