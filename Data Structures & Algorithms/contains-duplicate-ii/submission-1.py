class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        if k == 0:
            return False

        for L in range(0, len(nums)):
            for R in range(L+1, min(L+k+1, len(nums))):
                if nums[L] == nums[R]:
                    return True
        
        return False
        
        
