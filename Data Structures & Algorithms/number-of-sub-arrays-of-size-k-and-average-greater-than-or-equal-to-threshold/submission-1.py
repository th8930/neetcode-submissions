class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        
        count = 0
        dynamic_sum = sum(arr[:k])

        for L in range(len(arr)-k+1):
            if dynamic_sum / k >= threshold:
                count += 1
            
            if L + k < len(arr):
                dynamic_sum = dynamic_sum - arr[L] + arr[L+k]
        
        return count
