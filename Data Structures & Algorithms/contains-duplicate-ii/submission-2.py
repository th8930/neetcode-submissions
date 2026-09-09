class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 0:
            return False

        window = set()

        L = 0

        for R in range(L, len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
        
        return False
            