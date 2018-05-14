class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Babylonian method
        if x == 0:
            return 0

        x_last = x/2
        x_next = 1/2 * (x_last + x / x_last)
        
        while abs(x_last - x_next) >= 1:
            x_last = x_next
            x_next = 1/2 * (x_last + x / x_last)

        return int(x_next)
