class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = right = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit > max_profit:
                max_profit = profit

            while profit < 0:
                left += 1
                profit = prices[right] - prices[left]

            right += 1

        return max_profit