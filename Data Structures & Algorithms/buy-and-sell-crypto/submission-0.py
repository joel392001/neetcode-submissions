class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = prices[0]
        res = 0

        for price in prices:
            if price < best_price:
                best_price = price
            else:
                res = max(res, price - best_price)

        return res