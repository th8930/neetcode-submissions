class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        counts = defaultdict(int)
        length = 0
        max_frequency = 0
        L = 0

        for R in range(len(s)):
            counts[s[R]] += 1
            max_frequency = max(max_frequency, counts[s[R]])

            while R - L + 1 - max_frequency > k:
                counts[s[L]] -= 1
                L += 1
            
            length = max(length, R-L+1)
        
        
        return length
            
