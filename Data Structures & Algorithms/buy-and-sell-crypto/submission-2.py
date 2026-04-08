class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        diff = 0

        for i, price in enumerate(prices):
            if price < min:
                min = price
            if price - min > diff:
                diff = price - min

        return diff