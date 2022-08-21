class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            lookbehind = s[i-1] if i > 0 else ""
            lookahead = s[i+1] if (i+1) < len(s) else ""
            
            if s[i] == "M":
                # handle `CM` cases in the C section
                res += 1000
                i += 1
            
            elif s[i] == "D":
                res += 500
                i += 1
                
            elif s[i] == "C":
                if lookahead == "M":
                    res += 900
                    i += 2
                elif lookahead == "D":
                    res += 400
                    i += 2
                else:
                    res += 100
                    i += 1
                    
            elif s[i] == "L":
                res += 50
                i += 1
                
            elif s[i] == "X":
                if lookahead == "C":
                    res += 90
                    i += 2
                elif lookahead == "L":
                    res += 40
                    i += 2
                else:
                    res += 10
                    i += 1
                    
            elif s[i] == "V":
                res += 5
                i += 1
            
            elif s[i] == "I":
                if lookahead == "X":
                    res += 9
                    i += 2
                elif lookahead == "V":
                    res += 4
                    i += 2
                else:
                    res += 1
                    i += 1
                    
        return res
