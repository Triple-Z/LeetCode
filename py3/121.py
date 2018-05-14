class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profilt = None, 0
        if len(prices) > 0:
            min_price = prices[0]
        else:
            return 0

        for price in prices:
            if min_price > price:
                min_price = price
            
            if max_profilt < (price - min_price):
                max_profilt = price - min_price
            
        return max_profilt
