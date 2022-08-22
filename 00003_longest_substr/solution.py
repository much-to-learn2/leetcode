class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currWinner = ""
        buffer = ""
        h = {}
        i, j = 0, 0
        while j < len(s):
            currChar = s[j]
            if s[j] not in buffer:
                h[s[j]] = j
                buffer += s[j]
                j += 1
                
            else:
                i = h[s[j]] + 1
                if len(buffer) > len(currWinner):
                    currWinner = buffer
                    
                buffer = s[i:j]
                h[s[j]] = j
                
        if len(buffer) > len(currWinner):
            currWinner = buffer
                
        return len(currWinner)
