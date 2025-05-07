from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0
        minimum_price: int = prices[0]

        for price in prices:
            profit = price - minimum_price

            if max_profit < profit:
                max_profit = profit

            if price < minimum_price:
                minimum_price = price

        return max_profit
