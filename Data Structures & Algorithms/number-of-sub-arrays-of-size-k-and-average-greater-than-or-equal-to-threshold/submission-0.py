
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        
        count = 0
        for L in range(0, len(arr)-k+1):
            R = L + k
            sub_arr = arr[L:R]
            if sum(sub_arr) / k >= threshold:
                count += 1
        
        return count