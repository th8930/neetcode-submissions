class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        # length = 1
        # window = set([s[0]])
        length = 0
        window = set()
        L = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(length, R-L+1)
        
        return length
