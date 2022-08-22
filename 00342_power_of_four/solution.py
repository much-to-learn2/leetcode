class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        4^x = n === log4(n) = x
        if ^ the logarithmic expression is a whole number (x % 1 == 0)
        then n is a power of 4 (return True)
        """
        if n <= 0:
            return False
        import math
        return math.log(n, 4) % 1 == 0
