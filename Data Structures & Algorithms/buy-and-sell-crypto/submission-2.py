class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        l, r = 0, 1
        while r <= len(prices) - 1 :
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            elif profit >= 0:
                r += 1
                curr_profit = max(curr_profit, profit)
        return curr_profit

            
