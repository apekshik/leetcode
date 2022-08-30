class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        res = 0 

        l = 0 # left pointer for sliding window 
        for r in range(len(s)): # move right pointer r across entire input string s 
            # if key doesn't exist, get() returns 0 and new key is initialized to 1. 
            # else count for letter at s[r] is incremented by 1. 
            count[s[r]] = 1 + count.get(s[r], 0) 

            # while total number of replaceable letters in the window is 
            # greater than k, we can't form a contigous subarray of the same letter
            # via replacement, so we incremement left pointer till we clear the bound. 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1 

            res = max(res, r - l + 1) # windowSize max for current r is r - l + 1. 

        return res 
    
            
