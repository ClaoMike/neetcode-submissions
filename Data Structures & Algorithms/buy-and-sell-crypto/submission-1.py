class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = right = 0

        while right < len(prices):
            while prices[right] - prices[left] < 0:
                left += 1

            if prices[right] - prices[left] > max_profit:
                max_profit = prices[right] - prices[left]

            right += 1

        return max_profit